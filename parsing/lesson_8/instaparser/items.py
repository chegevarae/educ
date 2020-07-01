# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InstaparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    user_id = scrapy.Field()
    user_type = scrapy.Field()
    user_fid = scrapy.Field()
    user_name = scrapy.Field()
    user_full_name = scrapy.Field()
    user_userpic = scrapy.Field()


