#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors

# ==========================删除==========================

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='190066', db='scrapyDB', charset='utf8')
# 创建游标
cursor = conn.cursor()
# sql
id=1
sql="delete from user where id='%s'" % (id)

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()


