'''
Написать приложение, которое собирает основные новости с сайтов news.mail.ru, lenta.ru, yandex.news
Для парсинга использовать xpath.
Структура данных должна содержать:
- название источника,
- наименование новости,
- ссылку на новость,
- дата публикации
Сложить все новости в БД.
'''

import requests, re
from bs4 import BeautifulSoup as bs
from lxml import html
from pymongo import MongoClient
from datetime import datetime
from pprint import pprint

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['news']
db.news_lenta.drop()
db.news_mail.drop()
db.news_yandex.drop()


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


# https://lenta.ru/parts/news/
main_link = 'https://lenta.ru'
response = requests.get(main_link + '/parts/news/', headers=headers)
dom = html.fromstring(response.text)
blocks = dom.xpath("//div[@class='item news']")
print(f'\nlenta.ru, новостей: {len(blocks)}\n')
for block in blocks:
    try:
        tmp = {}
        tmp['title'] = block.xpath(".//a/text()")[1]
        link = main_link + block.xpath(".//a/@href")[1]
        tmp['link'] = link
        # Получаем дату новости
        response_n = requests.get(link, headers=headers)
        dom_n = html.fromstring(response_n.text)
        tmp['date_news'] = dom_n.xpath(".//div[contains(@class,'b-topic__info')]/time/@datetime")[0]

        db.news_lenta.insert_one(tmp)

    except Exception as e:
        print('Error:', e)
        continue


# https://news.mail.ru/politics/
main_link = 'https://news.mail.ru'
response = requests.get(main_link + '/politics/', headers=headers)
dom = html.fromstring(response.text)
blocks = dom.xpath("//div[@class='newsitem newsitem_height_fixed js-ago-wrapper js-pgng_item']")
print(f'\nmail.ru, новостей: {len(blocks)}\n')
for block in blocks:
    try:
        tmp = {}
        tmp['title'] = block.xpath(".//a[@class='newsitem__title link-holder']/span/text()")[0]
        link = main_link + block.xpath(".//a[@class='newsitem__title link-holder']/@href")[0]
        tmp['link'] = link
        # Получаем дату новости
        response_n = requests.get(link, headers=headers)
        dom_n = html.fromstring(response_n.text)
        tmp['date_news'] = dom_n.xpath(".//div[contains(@class,'breadcrumbs breadcrumbs_article js-ago-wrapper')]/span/span/span/@datetime")[0]

        db.news_mail.insert_one(tmp)

    except Exception as e:
        print('Error:', e)
        continue


# https://yandex.ru/news/rubric/politics
main_link = 'https://yandex.ru'
response = requests.get(main_link + '/news/rubric/politics', headers=headers)
dom = html.fromstring(response.text)
blocks = dom.xpath("//div[@class='story story_view_normal story_noimage']")
print(f'\nyandex.ru, новостей: {len(blocks)}\n')
for block in blocks:
    try:
        tmp = {}
        tmp['title'] = block.xpath(".//a[@class='link link_theme_black i-bem']/text()")[0]
        link = main_link + block.xpath(".//a[@class='link link_theme_black i-bem']/@href")[0]
        link = re.sub('(?i)\?.*?$', '', link)
        tmp['link'] = link
        # Получаем дату новости
        response_n = requests.get(link, headers=headers)
        dom_n = html.fromstring(response_n.text)
        date_news = dom_n.xpath(".//a[@class='link link_theme_grey link_agency i-bem']/@data-counter")[0]
        date_news = re.search('(?<=date=).*?(?=,)', date_news).group(0)
        tmp['date_news'] = datetime.utcfromtimestamp(int(date_news)).strftime("%Y-%m-%dT%H:%M:%S+03:00")

        db.news_yandex.insert_one(tmp)

    except Exception as e:
        print('Error:', e)
        continue



