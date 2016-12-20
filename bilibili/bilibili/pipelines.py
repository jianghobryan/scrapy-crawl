# -*- coding: utf-8 -*-
import pymysql
import logging

def dbhandler():
    con = pymysql.connect(db='pachong',
                         host='localhost',
                         user='root',
                         password="123456",
                         charset='utf8')
    return con
class BilibiliPipeline(object):
    def process_item(self, item, spider):
        con = dbhandler()
        cur = con.cursor()

        try:
            sql = "insert ignore bilibili(title,tit_episode, comment) values(%s, %s, %s)"
            lis  = (item['title'],item['tit_episode'],item['comment'])
            cur.execute(sql, lis)
            con.commit()
        except Exception as e:
            logging.info(e)
            con.rollback()
        finally:
            cur.close()
            con.close()



        return item
