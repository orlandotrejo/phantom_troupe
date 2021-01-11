# -*- coding: utf-8 -*-
import scrapy


class InfosecSpider(scrapy.Spider):
    name = 'infosec'
    allowed_domains = ['https://infosec-conferences.com/#2021january']
    start_urls = ['https://infosec-conferences.com/#2021january/']

    def parse(self, response):
        print("=== Crawling infosec-conferences Events ===")
        print("HTTP STATUS: "+str(response.status))
        print("\n")

        parrafos = response.css("p")
        eventos = parrafos[3:len(parrafos)]

        for e in eventos:


        #TO BE CONTINUED
        #eventos =

        print(eventos[3])
