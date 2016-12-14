# -*- coding: utf-8 -*-
import scrapy
import json
from meituan.items import MeituanItem
import time
from meituan.settings import *
import requests
from lxml import etree
import logging

header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
          'Referer':'http://www.meituan.com'}

class MeituansSpider(scrapy.Spider):
    name = "meituans"
    allowed_domains = ["meituan.com"]

    def start_requests(self):
        for city in citys:
            for meishi in meishis:
                curl = "http://{}.meituan.com/category/{}".format(city,meishi)
                yield scrapy.Request(curl, headers=header, callback=self.c_parse)


    def c_parse(self,response):
        req = response.xpath('//div[@class="J-scrollloader cf J-hub"]/@data-async-params').extract()[0]
        shopnums = json.loads(req)['data'].split("[")[1].split("]")[0].split(",")
        for shopnum in shopnums:
            durl = 'http://nj.meituan.com/shop/{}'.format(shopnum)
            yield scrapy.Request(durl, headers=header, callback=self.d_parse)

        next_page = response.xpath('//a[@gaevent="content/page/next"]/@href').extract()
        if next_page != []:
            yield scrapy.Request(response.urljoin(next_page[0]), headers=header,callback=self.c_parse)
            logging.info("下一页网址为： {}".format(response.urljoin(next_page[0])))
        else:
            pass


    def d_parse(self,response):
        item = MeituanItem()
        item['category'] = response.xpath('//a[@class="tag"]/text()')[0].extract()
        item['city'] = response.xpath('//a[@class="city-info__name"]/text()')[0].extract()
        item['name'] = response.xpath('//span[@class="title"]/text()')[0].extract()
        item['address'] = response.xpath('//span[@class="geo"]/text()')[0].extract()
        item['contact'] = response.xpath('//div[@class="fs-section__left"]/p[last()]/text()')[0].extract()
        item['evagrade'] = response.xpath('//span[@class="biz-level"]/strong/text()').extract_first(default="0")
        item['evanum'] = response.xpath('//a[@class="num rate-count"]/text()').extract_first(default="0")
        item['salelist']={}
        for sale in response.xpath('//ul[@class="onsale-list cf"]/li'):
            item['salelist'][sale.xpath('.//span[@class="title"]/text()').extract_first(default="0")] = sale.xpath('.//strong/text()').extract_first(default="0")
        yield item




