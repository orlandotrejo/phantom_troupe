# -*- coding: utf-8 -*-
import scrapy
from ..items import ItConferencesItem

class MicrofocusSpider(scrapy.Spider):
    name = 'microfocus'
    allowed_domains = ['https://www.microfocus.com/resources/events/']
    start_urls = ['https://www.microfocus.com/resources/events//']

    def parse(self, response):
        print("=== Crawling MicroFocus Events ===")
        print("HTTP STATUS: "+str(response.status))
        print("\n")

        eventos = response.css("div.events")

        for e in eventos:
            fecha_lugar = e.css("div.col-sm-2::text").getall()
            efecha = fecha_lugar[0].strip()
            elugar = fecha_lugar[1].strip()
            eurl = e.css("a::attr(href)").get()
            ename = e.css("a::text").get()

            items = ItConferencesItem()

            items['company'] = "Microfocus"
            items['location'] = elugar
            items['venue'] = " "
            items['date'] = efecha
            items['event'] = ename
            items['url'] = eurl

            yield items
