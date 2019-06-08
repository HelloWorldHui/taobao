# coding=utf
"""
author=Hui_T
"""
import pymongo
from setting import *

def Mongo_client(ip,port):
    db = pymongo.MongoClient(host=ip,port=port,username="root",password="123")
    # db.admin.auth("root",123)
    test  = {"test":1}
    db.spider.taobao.insert_one(test)

Mongo_client(Mongo_ip,Mongo_port)