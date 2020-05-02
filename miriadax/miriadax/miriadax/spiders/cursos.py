# -*- coding: utf-8 -*-
import scrapy
import json


class CursosSpider(scrapy.Spider):
    name = 'cursos'
    allowed_domains = ['miriadax.net/web/general-navigation/cursos']
    start_urls = ['http://miriadax.net/web/general-navigation/cursos/']

    def parse(self, response):
        print("\n")
        print("HTTP STATUS: "+str(response.status))
        print(response.css("title::text").get())
        print("\n")

        #This crawler does not include images. This can be changed!

        allCurso = response.css("div.curs-title")
        firstCurso = allCurso[0]
        titulo = firstCurso.css("a::text").get()
        url_titulo = firstCurso.css("a::attr(href)").get()

        allUniversity = response.css("div.university")
        firstUniversity = allUniversity[0]
        universidad = firstUniversity.css("a::text").get()
        url_universidad = firstUniversity.css("a::attr(href)").get()

        allFecha = response.css("div.university-date::text").getall()

        allLogo = response.css("div.courselogodiv")
        firstLogo = allLogo[0]
        logo = firstLogo.css("img::attr(src-data)").get()

        print(titulo)
        print(url_titulo)
        print(universidad)
        print("https://miriadax.net" + url_universidad)
        print(allFecha[0])
        print(logo)
