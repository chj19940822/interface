# -*- coding: utf-8 -*-
"""
------------------------------------
@Time    : 2020/6/28 12:42
@Author  : Destiny
@FileName: handle_mysql.py
@Software: PyCharm
------------------------------------
"""
import random
import pymysql

class HandleMysql:
    """

    """
    def __init__(self):
        self.conn = pymysql.connect(host='rm-bp1btllrpl19n08i9.mysql.rds.aliyuncs.com',
                                  user='test_user',
                                  password='userOF#test0726',
                                  port=3306,
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def get_value(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args=args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    do = HandleMysql()
    sql = "select * from db_trade.zcy_orders where limit 10"
    a = do.get_value(sql, is_more=True)
    print(a)
    pass