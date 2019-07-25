# -*- coding: utf-8 -*-
from scrapy.conf import settings
from pymongo import MongoClient


class JdphonePipeline(object):
    def __init__(self):
        # 获取setting中主机名，端口号和集合名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        col = settings['MONGODB_COL']

        # 创建一个mongo实例
        client = MongoClient(host=host,port=port)

        # 访问数据库
        db = client[dbname]

        # 访问集合
        self.col = db[col]

    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)
        return item