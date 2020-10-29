# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['http://quotes.toscrape.com/js']
    start_urls = ['http://http://quotes.toscrape.com/js/']

    def parse(self, response):
        pass
