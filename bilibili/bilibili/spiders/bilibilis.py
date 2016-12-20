# -*- coding: utf-8 -*-
import scrapy
import re,logging
from bilibili.items import BilibiliItem

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
          'Referer':'https://bilibili.com'}

class BilibilisSpider(scrapy.Spider):
    name = "bilibilis"
    allowed_domains = ["bilibili.com"]
    start_urls = (
        'http://www.bilibili.com/',
    )

    def start_requests(self):
        url = 'http://bangumi.bilibili.com/api/timeline_v2'
        yield scrapy.Request(url,headers=headers,callback=self.a_parse)

    def a_parse(self,response):
        session_id_list = re.findall(r'"season_id":(.*?),"season_status"', response.text)
        title_list = re.findall(r'"title":"(.*?)","url"',response.text)
        for session_id,title in zip(session_id_list, title_list):
            b_url = 'http://bangumi.bilibili.com/anime/'+ session_id
            yield scrapy.Request(b_url,headers=headers,callback=self.b_parse, meta={"title":title})

    def b_parse(self,response):
        episode_id_list = re.findall(r'data-episode-id="(.*?)"',response.text)
        title= response.meta["title"]
        tit_episode_list = re.findall(r'<a class="v1-complete-text" .*? title="(.*?)">',response.text)
        for episode_id, tit_episode in zip(episode_id_list, tit_episode_list):
            c_url = 'http://bangumi.bilibili.com/web_api/get_source'
            yield scrapy.FormRequest(c_url,headers=headers,formdata={'episode_id':episode_id},callback=self.c_parse,meta={"title":title,"tit_episode":tit_episode})

    def c_parse(self, response):
        title = response.meta["title"]
        tit_episode = response.meta["tit_episode"]
        cid =re.findall(r'"cid":(.*?),',response.text)[0]
        d_url = 'http://comment.bilibili.com/{}.xml?html5=1'.format(cid)
        yield scrapy.Request(d_url,headers=headers,callback=self.d_parse,meta={"title":title,"tit_episode":tit_episode})

    def d_parse(self,response):
        item = BilibiliItem()
        comment_list = re.findall('<d p=".*?">(.*?)</d>',response.text)
        for comment in comment_list:
            item['title']=response.meta['title']
            item['comment'] = comment
            item['tit_episode'] = response.meta['tit_episode']
            yield item



