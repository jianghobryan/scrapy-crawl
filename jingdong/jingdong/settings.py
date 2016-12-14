# -*- coding: utf-8 -*-

BOT_NAME = 'jingdong'

SPIDER_MODULES = ['jingdong.spiders']
NEWSPIDER_MODULE = 'jingdong.spiders'


ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 4

COOKIES_ENABLED = False

ITEM_PIPELINES = {
   'jingdong.pipelines.JingdongPipeline': 300,
}

Categorylist = ['平板电视', '空调', '冰箱', '洗衣机', '烟机/灶具', '热水器', '消毒柜/洗碗机', '冷柜/冰吧', '家庭影院', '电风扇', '净化器', '扫地机', '净水设备', '挂烫机', '冷风扇',  '榨汁机', '电压力锅', '电饭煲', '豆浆机', '微波炉', '电磁炉',  '剃须刀', '电吹风', '口腔护理','电动工具', '浴霸/排气扇', 'LED灯', '平板电视', '客厅空调', '净化器', '吸尘器', '饮水机', '加湿器', '平板电视', '卧室空调', '净化器', '加湿器', '吸尘器/地宝', '除螨机', '热水器', '剃须刀', '电吹风', '净水', '除湿机', '足浴盆', '烟机/灶具', '锅（电饭煲）', '消毒柜/洗碗机', '净水', '豆浆机', '微波炉', '迷你音响', '按摩器', '书房空调', '净化器', '加湿器', '吸尘器']
