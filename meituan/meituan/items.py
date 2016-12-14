# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanItem(scrapy.Item):
    category = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    contact = scrapy.Field()
    evagrade = scrapy.Field()
    evanum = scrapy.Field()
    salelist = scrapy.Field()

