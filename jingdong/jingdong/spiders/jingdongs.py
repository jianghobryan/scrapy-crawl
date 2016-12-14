# -*- coding: utf-8 -*-
import scrapy
from jingdong.items import JingdongItem
from jingdong.settings import Categorylist

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
          'Referer':'https://www.jd.com/'}

class JingdongsSpider(scrapy.Spider):
    name = "jingdongs"
    allowed_domains = ["jd.com"]

    def start_requests(self):
        for category in Categorylist:
            for page in range(1,30):
                c_url ='https://search.jd.com/s_new.php?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=4&stock=1&page={}&scrolling=y&pos=30'.format(category,page)
                yield scrapy.Request(c_url, headers=header,callback=self.c_parse,meta = {"category": category})

    def c_parse(self, response):
        item = JingdongItem()
        if response.status == 200:
            for data in response.xpath('//li[@class="gl-item"]'):
                item["category"] = response.meta["category"]
                item["name"] = data.xpath('./div/div[1]/a[1]/@title').extract_first(default="暂无")
                item["price"] = data.xpath('.//div[@class="p-price"]//i/text()').extract_first(default="暂无")
                item["evanum"] = data.xpath('.//div[@class="p-commit"]//a/text()').extract_first(default="暂无")
                item["buyscore"] = data.xpath('//div[@class="p-commit"]//em/text()').extract_first(default="暂无")
                item["url"] = data.xpath('./div/div[1]/a[1]/@href').extract_first(default="暂无")[2:]
                yield item
        else:
            pass

