#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors,time
import weatherHttp_2
import datetime
import sql_test_1

# ==========================插入==========================
# https://www.cnblogs.com/emanlee/p/4399147.html


def insertData(city, times, temp, wind, sd):

    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='190066', db='scrapyDB', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # sql

    effect_row = cursor.executemany(\
        "insert into weather(city,date,temp,wind,sd) values (%s,%s,%s,%s,%s)",\
        [(city, times, temp, wind, sd)])

    conn.commit()
    cursor.close()
    conn.close()
    # 获取自增id
    new_id = cursor.lastrowid
    print(new_id)


