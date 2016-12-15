# -*- coding: utf-8 -*-
import scrapy
import logging,json
from douban.items import DoubanItem
from douban.settings import Countrylist, Decadelist, Categorylist

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
          'Referer':'https://movie.douban.com'}


class DoubansSpider(scrapy.Spider):
    name = "doubans"
    allowed_domains = ["douban.com"]

    def start_requests(self):
        for country in Countrylist:
            for decade in Decadelist:
                for category in Categorylist:
                    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag={}%20{}%20{}&sort=recommend&page_limit=500&page_start=0'.format(country,decade,category)
                    yield scrapy.Request(url, headers=headers,callback=self.parse,meta={"country":country,"decade":decade,"category":category})

    def parse(self, response):
        item= DoubanItem()
        tres = json.loads(response.text)
        for e in tres["subjects"]:
            item['playable'], item['title'], item['rate'], item['url'] = e['playable'], e['title'], e['rate'], e['url']
            item["country"]=response.meta["country"]
            item['decade'] = response.meta['decade']
            item['category']=response.meta['category']
            yield item
