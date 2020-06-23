# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse        # Для подсказок объекта response
from jobparser.items import JobparserItem   # Подключаем класс из items

class HhruSpider(scrapy.Spider):
    name = 'hhru'                           # Имя паука
    allowed_domains = ['hh.ru']             # Домен в рамках которого работаем

    # Стартовая ссылка (точка входа)
    start_urls = ['https://spb.hh.ru/search/vacancy?clusters=true&enable_snippets=true&text=Data+scientist&L_save_area=true&area=2&from=cluster_area&showClusters=true']


    def parse(self, response:HtmlResponse):                                 # С этого метода все и начинается (в response - первый ответ)
        # Ищем ссылку для перехода на следующую страницу
        next_page = response.css('a.HH-Pager-Controls-Next.HH-Pager-Control::attr(href)').extract_first()

        # Ищем на полученной странице ссылки на вакансии
        vacansy_links = response.css('div.vacancy-serp div.vacancy-serp-item a.HH-LinkModifier::attr(href)').extract()
        for link in vacansy_links:                                          # Перебираем ссылки
            yield response.follow(link, callback=self.vacansy_parse)        # Переходим по каждой ссылке и обрабатываем ответ методом vacansy_parse

        yield response.follow(next_page, callback=self.parse)               # Переходим по ссылке на следующую страницу и возвращаемся к началу метода parse


    def vacansy_parse(self, response:HtmlResponse):                         # Здесь обрабатываем информацию по вакансии
        vlink = response.url                          # Ссылка на страницу вакансии
        vname = response.xpath('//h1//text()').extract_first()              # Получаем наименование вакансии
        vsalary = response.css('p.vacancy-salary span::text').extract()     # Получаем зарплату в виде списка отдельных блоков
        clink = 'https://spb.hh.ru' + response.css('div.vacancy-company-name-wrapper a::attr(href)').extract_first()    # Получаем ссылку на страницу компании
        vcomp = ''.join(response.css('div.vacancy-company-name-wrapper span.bloko-section-header-2::text').extract())   # Получаем название компании компании
        if len(clink) == 0:
            clink = response.css('p.vacancy-company-name-wrapper a::attr(href)').extract_first()    # Получаем ссылку на страницу компании
            vcomp = ''.join(response.css('p.vacancy-company-name-wrapper span.bloko-section-header-2::text').extract()) # Получаем название компании компании
        vgeo = ''.join(response.xpath('//p[@data-qa="vacancy-view-location"]//text()').extract())   # Получаем адрес компании
        exp_time = response.xpath('//div[@class="vacancy-description"]/div[1]//text()').extract()   # Получаем опыт и график
        vdescr = response.xpath('//div[@class="vacancy-description"]//text()').extract()    # Получаем описание вакансии
        vdate = response.xpath('//p[@class="vacancy-creation-time"]//text()').extract()     # Дата публикации
        yield JobparserItem(lnkpage=vlink, name=vname, salary=vsalary, link_company=clink, company=vcomp, geo=vgeo, experience=exp_time, descr=vdescr, date_pub=vdate) # Передаем данные в item для создания структуры json






