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

class TaobaoPipeline(object):
    def process_item(self, item, spider):
        con = dbhandler()
        cur = con.cursor()

        sql = "insert ignore into taobao(category,goodname,goodprice,buynum,sellorname,location) values(%s,%s,%s,%s,%s,%s) "
        lis = (item["category"],item['goodname'],item['goodprice'],item['buynum'],item['sellorname'],item['location'])
        try:
            cur.execute(sql, lis)
            con.commit()
        except Exception as e:
            logging.info(e)
            con.rollback()
        finally:
            cur.close()
            con.close()
        return item
