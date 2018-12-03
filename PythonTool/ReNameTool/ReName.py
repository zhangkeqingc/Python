# coding:utf-8
import os



def file_name(path):
    for root, dirs, files in os.walk(path):
        print('root',root)  #当前目录路径
        print('dirs',dirs)  #当前路径下所有子目录
        print('files',files) #当前路径下所有非目录子文件
        for name in files:
            print('name',name)
            new_name = '布撤防_' + name

            os.rename(path + name, path + new_name)


path = '/Users/frank/Desktop/Tool/'

file_name(path)
