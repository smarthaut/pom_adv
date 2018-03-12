#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 9:57
# @Author  : huanghe
# @Site    : 
# @File    : test_ad_materia.py
# @Software: PyCharm
import os
import sys
import unittest

import requests

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from baselib.db import mongo_db
import json

class AdMateriaTest(unittest.TestCase):


    def setUp(self):
        headers = {
            'Accept': 'application/json'
        }
        self.base_url = 'http://10.50.4.115:8080/aquapaas_adv/rest/ads/aditem/aditems'
        self.header = headers
        db = mongo_db.DB()
        self.collection = db.getConnection(table_name='aquapaas', connection_name='admateria')

    def tearDown(self):
        print(self.result)

    def get_and_post(self,type):
        content = self.collection.find({'type':type})[0]['content']
        r = requests.get(url=self.base_url,params=content,headers=self.header)
        result = []
        for i in r.json():
            result.append(i['name'])
        self.result = result
        return self.result

    def test_get_ad_img_materia(self):
        #状态为未审核的图文素材
        self.result = self.get_and_post('get_ad_materia_img_list')
        print('状态为未审核的图文素材名')

    def test_get_ad_video_materia(self):
        #状态为未审核的视频素材
        self.result = self.get_and_post('get_ad_materia_video_list')
        print('状态为未审核的视频素材名')

    def test_get_ad_word_materia(self):
        #状态为未审核的字幕素材
        self.result = self.get_and_post('get_ad_materia_subtitle_list')
        print('状态为未审核的字幕素材名')
