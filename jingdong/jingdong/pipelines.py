# -*- coding: utf-8 -*-
import pymysql
import logging

def dbhandler():
    con = pymysql.connect(db="pachong",
                          host="localhost",
                          user="root",
                          password="123456",
                          charset="utf8")
    return con

class JingdongPipeline(object):
    def process_item(self, item, spider):
        con = dbhandler()
        cur = con.cursor()
        sql = "insert ignore into jingdong(category,sname,price,evanum,buyscore,url) values(%s,%s,%s,%s,%s,%s)"
        lis = (item['category'],item["name"],item['price'],item['evanum'],item["buyscore"],item["url"])
        try:
            cur.execute(sql,lis)
            con.commit()
        except Exception as e:
            logging.info(e)
            con.rollback()
        finally:
            cur.close()
            con.close()
        return item
