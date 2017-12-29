#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors


# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='190066', db='scrapyDB', charset='utf8')
# 创建游标
cursor = conn.cursor()

effect_row = cursor.executemany("insert into weather(date,week,temperature,weather,wind)values(%s,%s,%s,%s,%s)", [("2017-12-23","周日","11","晴天","南风2级")])

conn.commit()
cursor.close()
conn.close()
#获取自增id
new_id = cursor.lastrowid
print(new_id)