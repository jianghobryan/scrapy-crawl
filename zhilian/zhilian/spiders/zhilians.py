# -*- coding: utf-8 -*-
import scrapy
from zhilian.items import ZhilianItem
from zhilian.settings import *
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
          'Referer': 'http: // sou.zhaopin.com / jobs / searchresult.ashx?pd = 7',
          'Upgrade - Insecure - Requests': '1'}

class ZhiliansSpider(scrapy.Spider):
    name = "zhilians"
    allowed_domains = ["zhaopin.com"]
    start_urls = (
        'http://sou.zhaopin.com/jobs/searchresult.ashx?pd=7',
    )

    def start_requests(self):
        item = ZhilianItem()

        for industry in dIndustry:
            for city in dCity:
                url =  'http://sou.zhaopin.com/jobs/searchresult.ashx?pd=7&jl={city}&in={industry}'.format(city = city,industry = industry)
                yield scrapy.Request(url, headers=header, callback = self.parse)

    def parse(self, response):
        item = ZhilianItem()
        for req in response.xpath('//table[@class="newlist"]')[1:]:
            item["jname"] = req.xpath('.//td[@class="zwmc"]//a/text()').extract()[0]
            item["cname"] = req.xpath('.//td[@class="gsmc"]/a/text()').extract()[0]
            item["salary"] = req.xpath('.//td[@class="zwyx"]/text()').extract()[0]
            item["workplace"] = req.xpath('.//td[@class="gzdd"]/text()').extract()[0]
            item["url"] = req.xpath('.//td[@class="zwmc"]//a/@href').extract()[0]
            yield item

        next_page = response.xpath('//a[@class="next-page"]/@href').extract()[0]
        if next_page:
            url = next_page
            time.sleep(2)
            yield scrapy.Request(url, callback=self.parse, headers=header)
        else:
            return


