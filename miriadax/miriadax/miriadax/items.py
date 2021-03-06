# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MiriadaxItem(scrapy.Item):
    # define the fields for your item here like:
    course_title = scrapy.Field()
    url_course = scrapy.Field()
    university = scrapy.Field()
    url_university = scrapy.Field()
    date = scrapy.Field()
    url_logo = scrapy.Field()
    pass
