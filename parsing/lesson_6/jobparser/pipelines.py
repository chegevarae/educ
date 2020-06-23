# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class JobparserPipeline:                            # Класс для обработки item'a
    def __init__(self):                             # Конструктор, где инициализируем подключение к СУБД
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.hh_scrapy


    def process_item(self, item, spider):           # Метод, куда прилетает сформированный item
        collection = self.mongo_base[spider.name]   # Выбираем коллекцию по имени паука
        # collection.insert_one(item)                 # Добавляем в базу данных
        if spider.name == 'hhru':                   # Здесь можно сделать обработку item в зависимости от имени паука
            collection.insert_one(item)             # Добавляем в базу данных
        if spider.name == 'sjru':                   # Здесь можно сделать обработку item в зависимости от имени паука
            collection.insert_one(item)             # Добавляем в базу данных
        return item

    def __del__(self):                              # Деструктор. Код в нем выполнится, перед уничтожением объекта, можно закрыть файл на запись
        pass


