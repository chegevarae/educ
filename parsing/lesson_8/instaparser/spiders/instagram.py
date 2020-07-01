# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from instaparser.items import InstaparserItem
import re, json
from urllib.parse import urlencode
from copy import deepcopy
# from w3lib.url import url_query_parameter # отлично работает для извлечения параметров ссылок


class InstagramSpider(scrapy.Spider):
    # Атрибуты класса
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://instagram.com/']
    insta_login = ''
    insta_pwd = ''
    inst_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    parse_user = 'clan_of_python'           # Пользователь, у которого собираем посты. Можно указать список

    graphql_url = 'https://www.instagram.com/graphql/query/?'
    query_hash_followers = 'c76146de99bb02f6415203be841dd25a'      # hash для получения данных о подписчиках
    query_hash_follow = 'd04b0a864b4b54837c0d870b0e77e076'         # hash для получения данных о подписках


    # Первый запрос на стартовую страницу
    def parse(self, response:HtmlResponse):
        csrf_token = self.fetch_csrf_token(response.text)   # csrf token забираем из html
        yield scrapy.FormRequest(                           # Заполняем форму для авторизации
            self.inst_login_link,
            method = 'POST',
            callback = self.user_parse,
            formdata = {'username':self.insta_login, 'enc_password':self.insta_pwd},
            headers = {'X-CSRFToken':csrf_token}
        )


    # Проверяем авторизацию и получаем страницу пользователя
    def user_parse(self, response:HtmlResponse):
        j_body = json.loads(response.text)
        if j_body['authenticated']:                         # Проверяем ответ после авторизации
            yield response.follow(                          # Переходим на желаемую страницу пользователя. Сделать цикл для кол-ва пользователей больше 2-ух
                f'/{self.parse_user}',
                callback = self.page_data_url_followers,
                cb_kwargs = {'username':self.parse_user}
            )


    # Получаем стартовую страницу
    def page_data_url_followers(self, response:HtmlResponse, username):
        user_id = self.fetch_user_id(response.text, username)       # Получаем id пользователя

        # Формируем ссылку для получения подписчиков:
        variables = {
            'id': user_id,
            'include_reel': True,
            'fetch_mutual': True,
            'first': 12}
        url_followers = f'{self.graphql_url}query_hash={self.query_hash_followers}&{urlencode(variables)}'
        yield response.follow(
            url_followers,
            callback = self.user_data_followers,
            # callback = self.user_data_pars,
            cb_kwargs = {'username':username,
                       'user_id':user_id,
                       'variables':deepcopy(variables)}             # variables ч/з deepcopy во избежание гонок
        )

        # Формируем ссылку для получения подписок:
        variables = {
            'id': user_id,
            'include_reel': True,
            'fetch_mutual': False,
            'first': 12}
        url_follow = f'{self.graphql_url}query_hash={self.query_hash_follow}&{urlencode(variables)}'
        yield response.follow(
            url_follow,
            callback = self.user_data_follow,
            # callback = self.user_data_pars,
            cb_kwargs = {'username':username,
                       'user_id':user_id,
                       'variables':deepcopy(variables)}             # variables ч/з deepcopy во избежание гонок
        )


    # Парсим подписчиков
    def user_data_followers(self, response:HtmlResponse,username,user_id,variables):   # Принимаем ответ. Не забываем про параметры от cb_kwargs
        j_data = json.loads(response.text)
        users = j_data.get('data').get('user').get('edge_followed_by').get('edges')     # Сами пользователи
        for user in users:                                                              # Перебираем юзеров, собираем данные
            item = InstaparserItem(
                user_id = user_id,
                user_type = 'followers',
                user_fid = user['node']['id'],
                user_name = user['node']['username'],
                user_full_name = user['node']['full_name'],
                user_userpic = user['node']['profile_pic_url']
            )
            yield item
        page_info = j_data.get('data').get('user').get('edge_followed_by').get('page_info')
        if page_info.get('has_next_page'):                                          # Если есть следующая страница
            variables['after'] = page_info['end_cursor']                            # Новый параметр для перехода на след. страницу
            url = f'{self.graphql_url}query_hash={self.query_hash_followers}&{urlencode(variables)}'
            yield response.follow(
                url,
                callback = self.user_data_followers,
                cb_kwargs = {'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables)}
            )


    # Парсим подписки
    def user_data_follow(self, response:HtmlResponse,username,user_id,variables):   # Принимаем ответ. Не забываем про параметры от cb_kwargs
        j_data = json.loads(response.text)
        users = j_data.get('data').get('user').get('edge_follow').get('edges')          # Сами пользователи
        for user in users:                                                              # Перебираем юзеров, собираем данные
            item = InstaparserItem(
                user_id = user_id,
                user_type = 'follow',
                user_fid = user['node']['id'],
                user_name = user['node']['username'],
                user_full_name = user['node']['full_name'],
                user_userpic = user['node']['profile_pic_url']
            )
            yield item
        page_info = j_data.get('data').get('user').get('edge_follow').get('page_info')
        if page_info.get('has_next_page'):                                          # Если есть следующая страница
            variables['after'] = page_info['end_cursor']                            # Новый параметр для перехода на след. страницу
            url = f'{self.graphql_url}query_hash={self.query_hash_follow}&{urlencode(variables)}'
            yield response.follow(
                url,
                callback = self.user_data_follow,
                cb_kwargs = {'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables)}
            )




    # Получаем токен для авторизации
    def fetch_csrf_token(self, text):
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')

    # Получаем id желаемого пользователя
    def fetch_user_id(self, text, username):
        matched = re.search('{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text).group()
        return json.loads(matched).get('id')