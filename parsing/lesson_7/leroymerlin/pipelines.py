# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy, os, re
from scrapy.pipelines.images import ImagesPipeline
from urllib.parse import urlparse
from pymongo import MongoClient

class DataBasePipeline:
    def __init__(self):                                     # Конструктор, где инициализируем подключение к СУБД
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.leroy_merlin

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]           # Выбираем коллекцию по имени паука
        collection.insert_one(item)                         # Добавляем в базу данных
        return item

class LeroyPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
       if item['photos']:
           for img in item['photos']:
               try:
                   yield scrapy.Request(img, meta=item)     # Скачиваем фото и передает item через meta
               except Exception as e:
                   print(e)

    def file_path(self, request, response=None, info=None):
        file_name = os.path.basename(urlparse(request.url).path)
        fname = file_name.split('.')
        folder = re.sub('_.*', '', fname[0])
        return folder + '/' + file_name

    def item_completed(self, results, item, info):
        if results:
           item['photos']=[itm[1] for itm in results if itm[0]]
        return item


