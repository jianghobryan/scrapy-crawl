import requests,threading,queue
from lxml import etree
import time
import pymysql

# 获取代理
def get_proxy():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
              'Referer': 'http: // www.xicidaili.com/nn/1'}
    raw_proxies = []
    # 抓取代理
    for page in range(2,102):
        url = 'http://www.xicidaili.com/nn/{}'.format(page)
        req = requests.get(url, headers = header)
        print(req.status_code,"注意，抓取中")
        e_req = etree.HTML(req.text)
        for i in e_req.xpath('//table[@id="ip_list"]//tr')[1:]:
            ip = i.xpath('.//td[2]/text()')[0]
            port = i.xpath('.//td[3]/text()')[0]
            proxy = {'http':'http://'+ip+":"+port}
            raw_proxies.append(proxy)
        time.sleep(3)
    return raw_proxies

# 检查代理是否有效
def check_proxy(proxies_list,count,timeout):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
              'Upgrade-Insecure-Requests':'1'}
    for proxy in proxies_list:
        try:
            # 页面成功打开，注意timeout设定，会影响代理有效数目
            req = requests.get("http://www.zhaopin.com", proxies= proxy, headers=header,timeout=timeout)
            if req.status_code == 200:
                checked_proxy.append(proxy)
                print(proxy,"有效，线程",count)
        except Exception:
            print(proxy, "无效，线程",count)
            continue

# 将代理存入mysql数据库中
def save_mysql():
    con = pymysql.connect(db = "pachong",
                          host = 'localhost',
                          user = 'root',
                          password = "123456",
                          charset = "utf8")
    cur = con.cursor()
    cur.execute("truncate proxies")
    con.commit()
    print("-----------------------清空proxies表-------------------------")
    for p in checked_proxy:
        try:
            sql = "insert proxies(proxy) values(%s)"
            lit=(r'{}'.format(p))
            cur.execute(sql,lit)
            print(p,"存入mysql中")
            con.commit()
        except Exception as e:
            print(e)
            con.rollback()
    cur.close()
    con.close()

# 主程序，开启多线程验证代理
def main(tnums, timeout):
    threads = []
    count = 1
    proxies = get_proxy()
    proxies_new = []

    # 按线程数将所有代理均匀分配给各线程
    se = int(len(proxies)/tnums)
    for i in range(1,tnums+1):
        proxies_new.append(proxies[(i-1)*se:i*se])

    for proxies_list in proxies_new:
        t = threading.Thread(target=check_proxy, args=[proxies_list,count,timeout])
        count += 1
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

    save_mysql()


if __name__ == "__main__":
    checked_proxy = []
    print("欢迎进入代理采集系统，请按指示操作")
    timeout = int(input("请设置链接超时时间（秒）： "))
    tnums = int(input("请设置线程数目： "))
    start = time.time()
    main(tnums,timeout)
    end = time.time()
    print("----结束----"*5,"用时{}秒".format(int(end-start)),"共采集{}个有效代理".format(len(checked_proxy)),sep="\n\n")
    print(checked_proxy)



