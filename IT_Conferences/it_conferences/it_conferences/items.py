# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItConferencesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    venue = scrapy.Field()
    date = scrapy.Field()
    event = scrapy.Field()
    url = company = scrapy.Field()
