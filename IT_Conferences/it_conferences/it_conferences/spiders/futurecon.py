# -*- coding: utf-8 -*-
import scrapy
from ..items import ItConferencesItem

class FutureconSpider(scrapy.Spider):
    name = 'futurecon'
    allowed_domains = ['https://futureconevents.com/events/']
    start_urls = ['https://futureconevents.com/events//']

    def parse(self, response):
        print("=== Crawling MicroFocus Events ===")
        print("HTTP STATUS: "+str(response.status))
        print("\n")

        eventos = response.css("ul.bz-events-list")

        ciudades = eventos[0].css("h2::text").getall()          #Regresa lista de las ciudades
        fechas = eventos[0].css("p.date-time::text").getall()   #Regresa lista de las fechas
        urls = eventos[0].css("a.button::attr(href)").getall()  #Regresa lista con los URL del evento y el sponsor
        urls = urls[::2]                                        #Guardamos solo el event url

        titulo = list()

        it = 0
        for c in ciudades:
            cs = c.split(",")
            titulo.append(cs[0] + " Cybersecurity Conference")
            it = it + 1

        print("Ciudades = " + str(len(ciudades)))
        print("Fechas = " + str(len(fechas)))
        print("URLs = " + str(len(urls)))
        print("Titulos = " + str(len(titulo)))
        print("If all have the same element numbers it is OK!")

        it = 0
        for it in range(len(ciudades)):
            items = ItConferencesItem()

            items['company'] = "FutureCon"
            items['location'] = ciudades[it]
            items['venue'] = " "
            items['date'] = fechas[it]
            items['event'] = titulo[it]
            items['url'] = "https://futureconevents.com" + urls[it]

            yield items
