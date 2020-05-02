# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MiriadaxItem(scrapy.Item):
    # define the fields for your item here like:
    course_name = scrapy.Field()
    course_url = scrapy.Field()
    university_name = scrapy.Field()
    university_url = scrapy.Field()
    date = scrapy.Field()
    logo = scrapy.Field()
    pass
