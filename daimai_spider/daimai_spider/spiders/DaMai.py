# -*- coding: utf-8 -*-
import scrapy


class DamaiSpider(scrapy.Spider):
    name = 'DaMai'
    allowed_domains = ['damai.cn']
    start_urls = ['http://damai.cn/']

    def parse(self, response):
        pass
