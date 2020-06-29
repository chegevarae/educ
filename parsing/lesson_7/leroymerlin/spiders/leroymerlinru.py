# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from leroymerlin.items import LeroyItem
from scrapy.loader import ItemLoader

class LeroymerlinruSpider(scrapy.Spider):
    name = 'leroymerlinru'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        self.start_urls = [f'https://spb.leroymerlin.ru/search/?q={search[0]}', f'https://spb.leroymerlin.ru/search/?q={search[1]}']

    def parse(self, response):
        ads_links = response.xpath('//div/a[@class="black-link product-name-inner"]')
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response:HtmlResponse):
        loader = ItemLoader(item=LeroyItem(), response=response)      # Работаем через item loader
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('photos', '//picture[@slot="pictures"]/img/@src')
        loader.add_xpath('parametrs1', '//dt[@class="def-list__term"]/text()')
        loader.add_xpath('parametrs2', '//dd[@class="def-list__definition"]/text()')
        loader.add_value('link', response.url)
        loader.add_xpath('price', '//span[@slot="price"]/text()')
        yield loader.load_item()

        # name = response.xpath('//h1/text()').extract_first()
        # photos = response.xpath('//picture[@slot="pictures"]/img/@src').extract()
        # parametrs1 = response.xpath('//dt[@class="def-list__term"]/text()').extract()
        # parametrs2 = response.xpath('//dd[@class="def-list__definition"]/text()').extract()
        # link = response.url
        # price = response.xpath('//span[@slot="price"]/text()').extract_first()
        # yield LeroyItem(name=name, photos=photos, parametrs1=parametrs1, parametrs2=parametrs2, link=link, price=price)

