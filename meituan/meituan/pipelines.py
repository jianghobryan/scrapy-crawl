# -*- coding: utf-8 -*-

import pymysql

def dbhandler():
    con = pymysql.connect(db="pachong",
                          host="localhost",
                          user = "root",
                          password="123456",
                          charset="utf8")
    return con


class MeituanPipeline(object):

    def process_item(self, item, spider):
        con = dbhandler()
        cur = con.cursor()
        sql="insert meituan(category,city,sname,address,contact,evagrade,evanum,salelist) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        lis = (item['category'],item['city'],item['name'],item['address'],item['contact'],item['evagrade'],item['evanum'],r'{}'.format(item['salelist']))
        try:
            cur.execute(sql,lis)
            con.commit()
        except Exception as e:
            print(e)
            con.rollback()
        finally:
            cur.close()
            con.close()
        return item
