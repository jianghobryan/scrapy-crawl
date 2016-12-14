# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TaobaoItem(scrapy.Item):
        category = scrapy.Field()
        goodname = scrapy.Field()
        goodprice = scrapy.Field()
        buynum = scrapy.Field()
        sellorname = scrapy.Field()
        location = scrapy.Field()