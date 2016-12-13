# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem
from lagou.settings import *
import json

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
          'Referer': 'http: //www.baidu.com',
          'Upgrade - Insecure - Requests': '1'}

class ZhiliansSpider(scrapy.Spider):
    name = "lagous"
    allowed_domains = ["lagou.com"]


    def start_requests(self):
        for industry in dIndustry:
            for city in dCity:
                for page in range(1,31):
                    url =  'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&city={city}&hy={industry}&pn={page}'.format(city=city,industry=industry,page=page)
                    yield scrapy.Request(url, headers=header, callback = self.parse)

    def parse(self, response):
        item = LagouItem()
        req = json.loads(response.body.decode("utf-8"))
        for i in req['content']['positionResult']['result']:
            item["jname"] = i['positionName']
            item["cname"] = i['companyFullName']
            item["salary"] = i['salary']
            item["workplace"] = i['city']
            item["url"] = 'https://www.lagou.com/jobs/{}.html'.format(i['positionId'])
            item["industry"] =  i['industryField']
            yield item

