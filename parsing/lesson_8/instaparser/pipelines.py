# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class InstaparserPipeline:
    def __init__(self):                             # Конструктор, где инициализируем подключение к СУБД
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.insta

    def process_item(self, item, spider):
        if item['user_type'] == 'followers':
            collection = self.mongo_base.followers
            collection.insert_one(item)                 # Добавляем в базу данных
        elif item['user_type'] == 'follow':
            collection = self.mongo_base.follow
            collection.insert_one(item)                 # Добавляем в базу данных
        return item
