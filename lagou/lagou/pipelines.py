# -*- coding: utf-8 -*-
import pymysql

def dbhandle():
    con = pymysql.connect(db = "pachong",
                          user = "root",
                          password = "123456",
                          charset = "utf8",
                          host = "localhost")
    return con

class LagouPipeline(object):

    def process_item(self, item, spider):
        con = dbhandle()
        cur = con.cursor()
        sql = "insert lagou(jname,industry,salary,workplace,cname,url) values(%s, %s, %s, %s, %s, %s)"
        lis = (item['jname'], item['industry'], item['salary'], item['workplace'], item['cname'], item['url'])
        try:
            cur.execute(sql, lis)
            con.commit()
        except Exception as e:
            print(e)
            con.rollback()
        finally:
            cur.close()
            con.close()
        return item
