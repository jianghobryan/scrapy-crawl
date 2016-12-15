# -*- coding: utf-8 -*-

import scrapy


class DoubanItem(scrapy.Item):
    country = scrapy.Field()
    decade = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    rate = scrapy.Field()
    playable = scrapy.Field()
    url = scrapy.Field()

