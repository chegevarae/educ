# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):       # Создаем структуру item'a
    _id = scrapy.Field()
    lnkpage = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    link_company = scrapy.Field()
    company = scrapy.Field()
    geo = scrapy.Field()
    experience = scrapy.Field()
    descr = scrapy.Field()
    date_pub = scrapy.Field()
