#!/usr/bin/python3
# encoding: utf-8
import os

class fileMerge():
    def __init__(self):
        print('init')
    def addFile(self, file = '', foldname = ''):
        if os.path.exists(foldname):
            print('存在文件夹')
        else:
            print('不存在文件夹')
            os.mkdir(foldname)
        # 获取根目录下的 blob 文件夹
        filepwd = os.getcwd() + '/' + foldname + '/'
        # 保存文件到 blob 目录
        file.save(filepwd + file.filename)
    # def mergeFile(self):
