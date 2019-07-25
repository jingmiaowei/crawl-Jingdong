# -*- coding: utf-8 -*-
from scrapy.conf import settings
from pymongo import MongoClient


class JdphonePipeline(object):
    def __init__(self):
        
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        col = settings['MONGODB_COL']

        
        client = MongoClient(host=host,port=port)

       
        db = client[dbname]

        
        self.col = db[col]

    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)
        return item
