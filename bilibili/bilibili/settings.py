# -*- coding: utf-8 -*-


BOT_NAME = 'bilibili'

SPIDER_MODULES = ['bilibili.spiders']
NEWSPIDER_MODULE = 'bilibili.spiders'

ROBOTSTXT_OBEY = False


DOWNLOAD_DELAY = 4

COOKIES_ENABLED = False

ITEM_PIPELINES = {
   'bilibili.pipelines.BilibiliPipeline': 300,
}
