#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys
import re
import json
import time


#
# 1、读取text文件中的字符串 并删除多余的空格和换行
#
def readFileString (fileName):

    str = ''
    file_object = open(fileName)
    try:
        all_the_text = file_object.read()
        contents1 = re.sub('[\r\n\t]', '', all_the_text)
        contents2 = contents1.replace(' ', '')
        # contents3 = contents2.replace('RESPONSE:', '')
        str = contents2

        # 获取到的json字符串
        # print(contents3)

    finally:
        file_object.close()

    return str



#
# 2、判断数据类型
#
def isClassName(content):

    # 判断是不是字典
    contentStr = str(type(content))
    classStr = re.sub('[<\'> ]', '', contentStr)
    typeStr = classStr.replace('class', '')

    return typeStr

    # var name:String = ""  //str
    # var name:Int = 0      //int
    # var name:float = 0.0  //float
    # var name:NameM?       //dict
    # var name:[NameM]=[]   //list



#
# 3、获取每个json中所有层次的dicionary数据  迭代算法
#
allfile = {}
def getSingleJsonAllLevelDicionary(dicts,key):

    keyStr = str(key) + 'M'
    allfile[keyStr] = dicts

    for (key,values) in dicts.items():
        # 判断是不是对象
        if isClassName(values) == 'dict': # 多层嵌套
            getSingleJsonAllLevelDicionary(values,key)
        if isClassName(values) == 'list': # 多层嵌套
            if len(values) > 0:
                val1 = values[0]
                if isClassName(val1) == 'dict':
                    getSingleJsonAllLevelDicionary(val1, key)

    return allfile



#
# 4、key dictionary  to  swift class content string
#
def toModelString(dicts,keyStr,inheritClass):

    # 1 类名称
    projectName = keyStr[0].upper() + keyStr[1:]

    contentls = 'class ' + projectName + ' : ' +  inheritClass + '\n{\n'

    for key, values in dicts.items():
        contentls = contentls + '    var' + ' ' + key + ':'

        if isClassName(values) == 'str':
            contentls = contentls + 'String = ""  // \n'

        elif  isClassName(values) == 'int' :
            contentls = contentls + 'Int = 0  // \n'

        elif isClassName(values) == 'float':
            contentls = contentls + 'Float = 0.0  // \n'

        elif isClassName(values) == 'dict':
            keyU = key[0].upper() + key[1:]
            contentls = contentls + keyU + '? // \n'

        elif isClassName(values) == 'list':  #[] [{}]
            if len(values) > 0:
                val1 = values[0]
                if isClassName(val1) == 'int':
                    contentls = contentls + '[Int] = [] // \n '
                elif isClassName(val1) == 'String':
                    contentls = contentls + '[String] = [] // \n '
                elif isClassName(val1) == 'float':
                    contentls = contentls + '[Float] = [] // \n '
                elif isClassName(val1) == 'dict':
                    keyU = key[0].upper() + key[1:] + 'M'
                    contentls = contentls + '[' + keyU + '] = [] // \n'
                else:
                    contentls = contentls + '[Any] = [] // \n '
            else:
                contentls = contentls + '[Any] = [] // \n '

    return contentls + '\n}'


#
#  all string contents split string list last to dictionary   倒数第二步骤
#
def fileContentToDictionary(contents):
    filePath = '/Users/frank/Desktop/CreateSwiftFile/'  # 文件的保存路径 倒数第一步骤
    list = re.split(r"REQUEST:|RESPONSE:", contents)
    if len(list) > 0:
        filePath = list[0]
        del list[0]
    if len(list) % 2 != 0:
        del list[0]
    # print('奇数', len(list))
    # else:
    #     print('偶数', len(list))

    allDic = {}
    for i in range(int(len(list) / 2)):
        dicts1 = json.loads(list[i * 2])
        dicts2 = json.loads(list[i * 2 + 1])
        keyStr = dicts1['method']
        # print(keyStr)
        # print(dicts2)
        #
        # print(Util.isClassName(keyStr))
        # print(Util.isClassName(dicts2))

        allDic[keyStr] = dicts2

    return (allDic,filePath)


# filePath     文件的保存路径       倒数第一步骤
# projectName  项目名称
# modelType    引用的框架
# className    类名
# jsonContent  文件正文

def mkdir_text(filePath,projectName,modelType,className,jsonContent):

    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    timestring = time.strftime("%Y/%m/%d", timeArray)
    yearstring = time.strftime("%Y年", timeArray)

    # 头文件包含的信息
    headstring = '\n// \n//  Created by Frank on ' + timestring + '\n//  Copyright © ' + yearstring + ' com.cn.identity . All rights reserved. \n// \n// \n\n'

    # 完整头部信息
    head = '//\n//  ' + className + '.swift\n//  ' + projectName + headstring + modelType

    file_name = filePath + str(className) + str('.txt')

    with open(file_name, 'w+') as f:
        f.write('\n' + head + jsonContent)





#
# 文件的后缀名的修改
#
def changeSuffix (filePath):

    files = os.listdir(filePath) #列出当前目录下所有的文件

    for filename in files:
        portion = os.path.splitext(filename)  # 分离文件名字和后缀
        print(portion)

        if portion[1] == ".txt":  # 根据后缀来修改,如无后缀则空
            newname = portion[0] + ".swift"  # 要改的新后缀
            os.chdir(filePath)    # 切换文件路径,如无路径则要新建或者路径同上,做好备份
            os.rename(filename, newname)

