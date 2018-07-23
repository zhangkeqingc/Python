#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

import JsonToModel
# 成品

pathstring = 'RESPONSE.txt'          # 资源文件
projectName = 'TYKoalaEnforcement'   # 项目名称
modelType = 'import UIKit\n\n'       # 引用的框架
inheritClass = 'NSObject'            # 继承类


filecontents = JsonToModel.readFileString(pathstring)
dic,filePath = JsonToModel.fileContentToDictionary(filecontents)



# for (key, values) in dic.items():
#
#     JsonToModel.allfile = {}
#     dic1 = JsonToModel.getSingleJsonAllLevelDicionary(values,key)
#     for (keys, value) in dic1.items():
#         key = keys[0].upper() + keys[1:]
#         jsonContent = JsonToModel.toModelString(value, key, inheritClass)
#         JsonToModel.mkdir_text(filePath, projectName, modelType, key, jsonContent)
#
#     print('==================================')
#
#
# JsonToModel.changeSuffix(filePath)
