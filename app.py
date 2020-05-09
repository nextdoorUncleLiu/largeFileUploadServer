#!/usr/bin/python3
# encoding: utf-8
from flask import Flask, request
import pymongo
from flask_debugtoolbar import DebugToolbarExtension

from fileMerge import fileMerge

app = Flask(__name__)
# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<replace with a secret key>'

toolbar = DebugToolbarExtension(app)

FileMerge = fileMerge()

FileMerge.mergeFile('1589020081327')

@app.route('/blob', methods = ['post'])
def blob():
    # 连接数据库
    def conectData():
        # 创建客户端
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        print(request)
        # 获取数据库
        db = client['flaskSql']
        # 获取集合
        collection = db['blob']

        results = collection.find()
        for result in results:
            print(result)
        FileMerge.addFile(request.files['file'], request.form['foldname'])

    conectData()
    return {
        'state': 200
    }
@app.route('/merge', methods = ['post'])
def merge():
    FileMerge.mergeFile(request.json['foldname'])
    return {
        'state': 200
    }