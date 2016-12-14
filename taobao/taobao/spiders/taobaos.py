# -*- coding: utf-8 -*-
import scrapy
import logging
from taobao.items import TaobaoItem
from taobao.settings import Categorylist
import re
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
          'Referer':'https://s.taobao.com/'}


class TaobaosSpider(scrapy.Spider):
    name = "taobaos"
    allowed_domains = ["taobao.com"]

    def start_requests(self):
        for category in Categorylist:
            #虽然最大页面数为100，事实上一个查找最多可以抓取10168条数据也就是169页，可通过条件细分抓取更多数据
            for page in range(0,101):
                c_url = 'https://s.taobao.com/list?q={}&seller_type=taobao&bcoffset=12&s={}'.format(category,page*60)
                yield scrapy.Request(c_url, headers=header, callback=self.c_parse, meta={"category":category})

    def c_parse(self, response):
        item = TaobaoItem()
        if response.status == 200:
            c = response.text
            d = re.findall(r'"auctions":\[(.*)\].*,"recommendAuctions"', c, re.I | re.M | re.S)[0]
            e = re.sub(r"\\u003c.*?\\u003e", "", d)
            f = re.sub(r"\\u003d", "=", e)
            g = re.sub(r"\\u0026", "&", f)
            for i in g.split(r'{"i2iTags":')[1:]:
                item['goodname'] = re.findall(r'raw_title":"(.*)","pic_url', i)[0]
                item['goodprice'] = re.findall(r'view_price":"(.*)","view_fee', i)[0]
                item['buynum'] = re.findall(r'view_sales":"(.*)人付款', i)[0]
                item['sellorname'] = re.findall(r'nick":"(.*)","shopcard', i)[0]
                item['location'] = re.findall(r'item_loc":"(.*)","reserve_price', i)[0]
                item["category"] = response.meta["category"]
                yield item
        else:
            pass
