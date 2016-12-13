# -*- coding: utf-8 -*-

import scrapy

class ZhilianItem(scrapy.Item):
    jname = scrapy.Field()
    cname = scrapy.Field()
    salary = scrapy.Field()
    workplace = scrapy.Field()
    url = scrapy.Field()
    industry= scrapy.Field()
