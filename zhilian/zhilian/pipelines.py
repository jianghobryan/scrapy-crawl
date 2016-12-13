# -*- coding: utf-8 -*-
import pymysql

def dbhandle():
    con = pymysql.connect(host="localhost",
                          user = "root",
                          password = "123456",
                          charset = "utf8",
                          db = "pachong")
    return con

class ZhilianPipeline(object):
    def process_item(self, item, spider):
        con = dbhandle()
        cur = con.cursor()
        sql = "insert into zhilian(jname,cname,salary,workplace,url) values(%s,%s,%s,%s,%s)"
        lis = [item['jname'], item['cname'], item['salary'], item['workplace'], item['url']]

        try:
            cur.execute(sql,lis)
            con.commit()
        except Exception as e:
            print(e)
            con.rollback()
        return item
