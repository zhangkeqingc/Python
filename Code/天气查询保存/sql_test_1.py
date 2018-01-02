#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors

# ==========================查询==========================

def queryAllData():

    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='190066', db='scrapyDB', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # sql
    cursor.execute("select * from weather")

    # 获取剩余结果的第一行数据
    # row_1 = cursor.fetchone()
    # print(row_1)

    # 获取剩余结果前n行数据
    # row_2 = cursor.fetchmany(3)
    # print(row_2)

    # 获取剩余结果所有数据
    row_3 = cursor.fetchall()
    # print(row_3[0][3]) id date img temp weather wind city sd

    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    return row_3


queryAllData()