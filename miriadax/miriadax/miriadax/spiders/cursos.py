# -*- coding: utf-8 -*-
import scrapy
import json

from ..items import MiriadaxItem

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

        allCurso = response.css("div.name")                       #Regresa Lista de Cursos
        titulo = allCurso.css("a::text").getall()
        url_titulo = allCurso.css("a::attr(href)").getall()

        allUniversity = response.css("div.university")                  #Regresa Lista de Universidades
        universidad = allUniversity.css("a::text").getall()
        url_universidad = allUniversity.css("a::attr(href)").getall()

        allFecha = response.css("div.university-date::text").getall()   #Regresa Lista de Fechas

        allLogo = response.css("div.courselogodiv")                     #Regresa Lista de Logos
        logo = allLogo.css("img::attr(src-data)").getall()

        print(titulo)
        print(url_titulo)
        print(universidad)
        print(url_universidad)
        #print("https://miriadax.net" + url_universidad)
        print(allFecha)
        print(logo)
