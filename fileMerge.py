#!/usr/bin/python3
# encoding: utf-8
import os, re, shutil

class fileMerge():
    def __init__(self):
        print('init')
    def addFile(self, file = '', foldname = ''):
        saveFilePath = "blob/%s" % (foldname)
        if not os.path.exists('blob'):
            os.mkdir('blob')
        if not os.path.exists(saveFilePath):
            os.mkdir(saveFilePath)
        # 获取根目录下的 blob 文件夹
        blobpwd = "%s/blob/%s/" % (os.getcwd(), foldname)
        # 保存文件到 blob 目录
        file.save(blobpwd + file.filename)
    def mergeFile(self, foldname = ''):
        # 是否存在 file 文件夹
        if not os.path.exists('file'):
            os.mkdir('file')
        # 合并文件夹路径
        filepwd = "%s/file/" % (os.getcwd())
        # 创建合并文件
        saveFile = open(foldname, "wb+")
        # 文件名
        filename = None
        # 后缀名
        suffix = None
        # 切片文件的位置
        blobpwd = "%s/blob/%s/" % (os.getcwd(), foldname)
        # 遍历每一个切片文件
        for file in os.listdir(blobpwd):
            if (filename is None) and (suffix is None):
                fileInfo = os.path.splitext(file)
                filename = re.sub('\S[-]', "", fileInfo[0])
                suffix = fileInfo[1]
            # 读取切片文件内容
            fileContent = open(os.path.join(blobpwd, file), 'rb')
            # 写入到合并文件
            saveFile.write(fileContent.read())
        os.rename(foldname, "%s-%s%s" % (filename, foldname, suffix))