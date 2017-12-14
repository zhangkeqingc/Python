#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys

import Util


projectName = 'TYKoalaEnforcement'                  # 项目名称
modelType = 'import UIKit\n\n'                      # 引用的框架
inheritClass = 'NSObject'

pathstring = '/Users/frank/Desktop/CreateSwiftFile/JsonFile'

contents = Util.readFileString(pathstring)
dic,filePath = Util.fileContentToDictionary(contents)


for (key,value) in dic.items():
    # print(key)
    # print(Util.isClassName(value))
    jsonContent = Util.toModelString(value,key,inheritClass)
    Util.mkdir_text(filePath,projectName,modelType,key,jsonContent)


Util.changeSuffix(filePath)
