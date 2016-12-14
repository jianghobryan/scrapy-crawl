# -*- coding: utf-8 -*-

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 6
COOKIES_ENABLED = False

ITEM_PIPELINES = {
   'taobao.pipelines.TaobaoPipeline': 300,
}

Categorylist = ['项链', '手链', '发饰', '耳饰', '戒指', '新娘配饰', 'DIY饰品', '首饰盒', '翡翠', '黄金', '钻石', '金条', '珍珠', '琥珀', '和田玉', '铂金/PT', '石英表', '电子表', '机械表', '情侣表', '儿童表', '时装表', '光能表', '手表配件', '太阳镜', '光学镜', '司机镜', '运动镜', '护目镜', '配件', 'zippo', '瑞士军刀', '烟具', '酒具', '紫檀', '沉香木', '佛珠/手串', '品牌打火机', '紫砂', '文房', '核雕', '脸谱', '印章', '徽章', '西洋收藏', '流行珍藏']

