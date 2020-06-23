# -*- coding: utf-8 -*-
import scrapy
import json

from ..items import MiriadaxItem

class CursosSpider(scrapy.Spider):
    name = 'cursos'
    #allowed_domains = ['miriadax.net/web/general-navigation/cursos']
    #start_urls = ['http://miriadax.net/web/general-navigation/cursos/']

    allowed_domains = ['file:///C:/Users/otrej/AppData/Local/Temp/tmpwe9u1vgh.html']
    start_urls = ['file:///C:/Users/otrej/AppData/Local/Temp/tmpwe9u1vgh.html']

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

        #print(titulo)
        #print(url_titulo)
        #print(universidad)
        #print("https://miriadax.net" + url_universidad)
        #print(allFecha)
        #print(logo)

        print(len(titulo))
        print(len(url_titulo))
        print(len(universidad))
        print(len(url_universidad))
        print(len(allFecha))
        print(len(logo))

        if (len(titulo) == len(url_titulo) == len(universidad) == len(url_universidad) == len(allFecha) == len(logo)):
            print("OK Todos con el mismo número")
        else:
            print("ERROR: Datos con números diferentes")

        it = 0
        for it in range(len(titulo)):

            #print(titulo[it])
            #print(url_titulo[it])
            #print(universidad[it])
            #print("https://miriadax.net" + url_universidad[it])
            #print(allFecha[it])
            #print(logo[it])

            items = MiriadaxItem()

            items['course_title'] = titulo[it]
            items['url_course'] = url_titulo[it]
            items['university'] = universidad[it]
            items['url_university'] = str(("https://miriadax.net" + url_universidad[it]))
            items['date'] = allFecha[it]
            items['url_logo'] = logo[it]

            yield items
