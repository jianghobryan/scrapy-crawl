# -*- coding: utf-8 -*-

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'


ROBOTSTXT_OBEY = False

# CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 3

COOKIES_ENABLED = True


DEFAULT_REQUEST_HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
          'Referer': 'http: // www.lagou.com',
          'Upgrade - Insecure - Requests': '1'}





ITEM_PIPELINES = {
   'lagou.pipelines.LagouPipeline': 300,
}

dIndustry = ['移动互联网', '电子商务', '金融', '企业服务', '教育', '文化娱乐', '游戏', 'O2O', '硬件', '社交网络', '旅游', '医疗健康', '生活服务', '信息安全', '数据服务', '广告营销', '分类信息', '招聘', '其他']
dCity = ['北京', '上海', '广东', '广州', '韶关', '深圳', '珠海', '汕头', '佛山', '江门', '湛江', '茂名', '肇庆', '惠州', '梅州', '汕尾', '河源', '阳江', '清远', '东莞', '中山', '潮州', '揭阳', '云浮', '台山', '普宁', '南沙开发区', '开平', '龙川', '鹤山', '天津', '湖北', '武汉', '黄石', '十堰', '宜昌', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州', '恩施', '公安', '武穴', '天门', '仙桃', '潜江', '宜城', '神农架', '陕西', '西安', '铜川', '宝鸡', '咸阳', '渭南', '延安', '汉中', '榆林', '安康', '商洛', '兴平', '杨凌', '四川', '成都', '自贡', '攀枝花', '泸州', '德阳', '绵阳', '广元', '遂宁', '内江', '乐山', '南充', '眉山', '宜宾', '广安', '达州', '雅安', '巴中', '资阳', '阿坝', '甘孜', '凉山', '峨眉', '西昌', '简阳', '辽宁', '大连', '沈阳', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '阜新', '辽阳', '盘锦', '铁岭', '朝阳', '葫芦岛', '兴城', '海城', '昌图', '开原', '吉林', '长春', '珲春', '吉林市', '四平', '辽源', '通化', '白山', '松原', '白城', '延边', '公主岭', '江苏', '南京', '苏州', '昆山', '常熟', '张家港', '无锡', '江阴', '徐州', '常州', '南通', '连云港', '淮安', '盐城', '扬州', '镇江', '泰州', '靖江', '宿迁', '太仓市', '句容', '宜兴', '如皋', '丹阳', '扬中', '高邮', '启东', '泰兴', '溧阳', '盱眙', '通州', '金湖', '山东', '济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '莱芜', '临沂', '德州', '聊城', '滨州', '菏泽', '荣成', '黄岛', '乳山', '城阳', '即墨', '肥城', '兖州', '海阳', '胶州', '胶南', '平度', '莱西', '浙江', '杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水', '玉环县', '义乌', '平湖', '永康', '东阳', '嘉善', '余姚', '慈溪', '乐清', '永嘉', '桐乡', '瑞安', '温岭', '上虞', '诸暨', '海宁', '宁海', '三门', '德清', '象山', '方家山', '龙泉', '广西', '南宁', '柳州', '桂林', '梧州', '北海', '防城港', '钦州', '贵港', '玉林', '百色', '贺州', '河池', '来宾', '崇左', '安徽', '合肥', '芜湖', '蚌埠', '淮南', '马鞍山', '淮北', '铜陵', '安庆', '黄山', '滁州', '阜阳', '宿州', '巢湖', '六安', '亳州', '池州', '宣城', '凤阳', '广德', '宿松', '河北', '石家庄', '唐山', '秦皇岛', '邯郸', '邢台', '保定', '张家口', '承德', '沧州', '廊坊', '衡水', '燕郊开发区', '固安', '遵化', '香河', '三河', '山西', '太原', '大同', '阳泉', '长治', '晋城', '朔州', '晋中', '运城', '忻州', '临汾', '吕梁', '永济市', '和顺', '内蒙古', '呼和浩特', '包头', '乌海', '赤峰', '通辽', '鄂尔多斯', '呼伦贝尔', '兴安盟', '锡林郭勒盟', '乌兰察布', '巴彦淖尔', '阿拉善盟', '乌审旗', '满洲里', '黑龙江', '哈尔滨', '齐齐哈尔', '鸡西', '鹤岗', '双鸭山', '大庆', '伊春', '佳木斯', '七台河', '牡丹江', '黑河', '绥化', '大兴安岭', '安达', '双城', '尚志', '绥芬河', '肇东市', '福建', '福州', '厦门', '莆田', '三明', '泉州', '泉港区', '漳州', '南平', '龙岩', '宁德', '福安', '晋江', '江西', '南昌', '景德镇', '萍乡', '九江', '新余', '鹰潭', '赣州', '吉安', '宜春', '抚州', '上饶', '河南', '郑州', '开封', '洛阳', '平顶山', '安阳', '鹤壁', '新乡', '焦作', '濮阳', '许昌', '漯河', '三门峡', '南阳', '商丘', '信阳', '周口', '驻马店', '济源', '西平', '长葛', '湖南', '长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '郴州', '永州', '怀化', '娄底', '湘西', '海南', '海口', '三亚', '洋浦市/洋浦经济开发区', '琼海', '儋州', '五指山', '文昌', '万宁', '东方', '定安', '屯昌', '澄迈', '临高', '琼中', '保亭', '白沙', '昌江', '乐东', '陵水', '重庆', '贵州', '贵阳', '六盘水', '遵义', '安顺', '铜仁', '黔西南', '毕节', '黔东南', '黔南', '云南', '昆明', '曲靖', '玉溪', '保山', '昭通', '楚雄', '红河', '文山', '思茅', '西双版纳', '大理', '德宏', '丽江', '怒江', '迪庆', '临沧', '普洱', '西藏', '拉萨', '昌都', '山南', '日喀则', '那曲', '阿里', '林芝', '甘肃', '兰州', '嘉峪关', '金昌', '白银', '天水', '武威', '张掖', '平凉', '酒泉', '庆阳', '定西', '陇南', '临夏', '甘南', '青海', '西宁', '海东', '海北', '黄南', '海南州', '果洛', '玉树', '海西', '宁夏', '银川', '石嘴山', '吴忠', '固原', '中卫', '新疆', '乌鲁木齐', '克拉玛依', '吐鲁番', '哈密', '昌吉', '博尔塔拉', '巴音郭楞', '阿克苏', '克孜勒苏', '喀什', '和田', '伊犁', '塔城', '阿勒泰', '石河子', '奎屯市', '乌苏', '阿拉尔', '图木舒克', '五家渠', '香港', '澳门', '台湾省', '国外', '阿根廷', '澳大利亚', '奥地利', '白俄罗斯', '比利时', '巴西', '保加利亚', '加拿大', '塞浦路斯', '捷克', '丹麦', '埃及', '芬兰', '法国', '德国', '希腊', '匈牙利', '冰岛', '印度', '印度尼西亚', '爱尔兰', '以色列', '意大利', '日本', '韩国', '科威特', '马来西亚', '荷兰', '新西兰', '挪威', '巴基斯坦', '波兰', '葡萄牙', '俄罗斯联邦', '沙特阿拉伯', '新加坡', '南非', '西班牙', '瑞典', '瑞士', '泰国', '土耳其', '乌克兰', '阿联酋', '英国', '美国', '越南', '安哥拉', '加纳', '尼日利亚', '坦桑尼亚', '乌干达', '阿尔及利亚', '塞内加尔', '其他']

