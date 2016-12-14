# -*- coding: utf-8 -*-

import scrapy


class JingdongItem(scrapy.Item):
    category = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    evanum = scrapy.Field()
    buyscore = scrapy.Field()
    url = scrapy.Field()