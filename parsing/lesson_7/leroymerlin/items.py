# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader.processors import Compose, MapCompose, TakeFirst              # Подключаем обработчики
import scrapy

def cleaner_photo(value):                                               # Функция для изменения ссылок фотографий
    if value[:2] == '//':
        return f'http:{value}'
    return value

def strip_params(value):
    return value.strip()

def takeFirst2Int(value):
    return int(value[0].replace(' ', ''))

class LeroyItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    # Применяем обработчики
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(cleaner_photo))
    parametrs1 = scrapy.Field(output_processor=MapCompose(strip_params))
    parametrs2 = scrapy.Field(output_processor=MapCompose(strip_params))
    link = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(takeFirst2Int), output_processor=TakeFirst())
    # Без применения обработчиков
    # name = scrapy.Field()
    # photos = scrapy.Field()
    # parametrs1 = scrapy.Field()
    # parametrs2 = scrapy.Field()
    # link = scrapy.Field()
    # price = scrapy.Field()


