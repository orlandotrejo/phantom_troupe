# -*- coding: utf-8 -*-
import scrapy


class EventsSpider(scrapy.Spider):
    name = 'events'
    allowed_domains = ['https://www.sherpadesk.com/blog/top-it-conferences-2019-that-you-should-go-pt1']
    start_urls = ['http://https://www.sherpadesk.com/blog/top-it-conferences-2019-that-you-should-go-pt1/']

    def parse(self, response):
        pass
