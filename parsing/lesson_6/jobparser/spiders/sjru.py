# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse        # Для подсказок объекта response
from jobparser.items import JobparserItem   # Подключаем класс из items

class SjruSpider(scrapy.Spider):
    name = 'sjru'                                   # Имя паука
    allowed_domains = ['superjob.ru']               # Домен в рамках которого работаем

    # Стартовая ссылка (точка входа)
    start_urls = ['https://russia.superjob.ru/vacancy/search/?keywords=Python']


    def parse(self, response:HtmlResponse):                                 # С этого метода все и начинается (в response - первый ответ)
        # Ищем ссылку для перехода на следующую страницу
        next_page = response.css('a.f-test-link-Dalshe::attr(href)').extract_first()

        # Ищем на полученной странице ссылки на вакансии
        vacansy_links = response.xpath("//a[contains(@class,'icMQ_ _6AfZ9 f-test-link')]/@href").extract()
        for link in vacansy_links:                                          # Перебираем ссылки
            yield response.follow(link, callback=self.vacansy_parse)        # Переходим по каждой ссылке и обрабатываем ответ методом vacansy_parse

        yield response.follow(next_page, callback=self.parse)               # Переходим по ссылке на следующую страницу и возвращаемся к началу метода parse


    def vacansy_parse(self, response:HtmlResponse):                         # Здесь обрабатываем информацию по вакансии
        vlink = response.url                                                # Ссылка на страницу вакансии
        vname = response.xpath('//h1//text()').extract_first()              # Получаем наименование вакансии
        vsalary = response.css('span._1OuF_.ZON4b span::text').extract()    # Получаем зарплату в виде списка отдельных блоков
        clink = 'https://russia.superjob.ru' + response.xpath("//div/a[contains(@class,'_2JivQ')]/@href").extract_first()   # Получаем ссылку на страницу компании
        vcomp = ''.join(response.xpath('//a/h2[@class="_3mfro PlM3e _2JVkc _2VHxz _3LJqf _15msI"]//text()').extract())      # Получаем название компании компании
        vgeo = ''.join(response.css('span._6-z9f span::text').extract())    # Получаем адрес компании
        exp_time = ' '.join(response.xpath('//span/span/span[@class="_3mfro _1hP6a _2JVkc"]//text()').extract())     # Получаем опыт и график
        vdescr = response.xpath('//span[@class="_3mfro _2LeqZ _1hP6a _2JVkc _2VHxz _15msI"]//text()').extract()     # Получаем описание вакансии
        vdate = response.xpath('//div[@class="f-test-title _183s9 _3wZVt OuDXD _1iZ5S"]//span//text()').extract()   # Дата публикации
        yield JobparserItem(lnkpage=vlink, name=vname, salary=vsalary, link_company=clink, company=vcomp, geo=vgeo, experience=exp_time, descr=vdescr, date_pub=vdate) # Передаем данные в item для создания структуры json






