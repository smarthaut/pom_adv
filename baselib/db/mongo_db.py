#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 10:11
# @Author  : huanghe
# @Site    : 
# @File    : mongo_db.py
# @Software: PyCharm

import pymongo
import os
import configparser as cparser

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "baselib/db/db_config.ini"


cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get('mongoconf','host')
port = cf.get('mongoconf','port')
user = cf.get('mongoconf','user')
password = cf.get('mongoconf','password')


class DB:

    def __init__(self):
        try:
            self.client = pymongo.MongoClient(host,port=int(port))
        except :
            print('数据库连接失败')

    def getConnection(self,table_name,connection_name):
        db = self.client.get_database(table_name)
        svod = db.get_collection(connection_name)
        return svod




#client = pymongo.MongoClient(host,port=int(port))
#db = client.aquapaas
#svod = db.svod
#for id in svod.find():
    #print(id['url'])
    #print(id['content'])
