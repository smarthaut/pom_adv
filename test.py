#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 15:50
# @Author  : huanghe
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import os
import sys
import requests

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from baselib.db import mongo_db
import json

headers = {
    'Accept': 'application/json'
}
base_url = 'http://10.50.4.115:8080/aquapaas_adv/rest/ads/aditem/aditems'
header = headers
db = mongo_db.DB()
collection = db.getConnection(table_name='aquapaas', connection_name='admateria')
#content = collection.find({'type': 'get_ad_materia_list'})[0]['content']
#print(json.dumps(content))
content = {'type': 'img', 'user_type': '1', 'user_id': '000059370018BAE3073BE5FEDF4C9F4486A56916D6D5D20290', 'state': 'first_audit:prepare_audit'}
r = requests.get(url=base_url, params=content, headers=header)
result = r.json()
b = []
for i in result:
    b.append(i['name'])
print(b)
