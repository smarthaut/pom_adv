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
        ad_id= []
        for i in r.json():
            result.append(i['name'])
            ad_id.append(i['ad_id'])
        self.result = result
        self.ad_id = ad_id
        return self.result,self.ad_id

    '''def test_get_ad_img_materia(self):
        #状态为未审核的图文素材
        self.result = self.get_and_post('get_ad_materia_img_list')[0]
        print('状态为未审核的图文素材名')

    def test_get_ad_video_materia(self):
        #状态为未审核的视频素材
        self.result = self.get_and_post('get_ad_materia_video_list')[0]
        print('状态为未审核的视频素材名')

    def test_get_ad_word_materia(self):
        #状态为未审核的字幕素材
        self.result = self.get_and_post('get_ad_materia_subtitle_list')[0]
        print('状态为未审核的字幕素材名')'''

    #def test_sucai_shenhe(self):
        #ad_id = self.get_and_post('get_ad_materia_img_list')
        #self.exurl = 'http://10.50.4.115:8080/aquapaas/rest/auditflow/instance/ad_item/'

    '''def test_get_po(self):
        content = {'attribute':'ote_get_product_offering','product_offering_id':'54'}
        url = 'http://10.50.3.113:8040/STBServlet'
        r = requests.get(url=url, params=content, headers=self.header)
        print(r.status_code)
        self.result = r.text'''


    def test_sucai_shenhe(self):

        ad_id = self.get_and_post('get_ad_materia_subtitle_list')[1][0]
        print('审核通过ad_id为%s的字幕广告'% ad_id)
        exl_url = 'http://10.50.4.115:8080/aquapaas/rest/auditflow/instance/ad_item/'+ad_id
        content = self.collection.find({'type': 'sucai_shenhe'})[0]['content']
        date = {"no":"1","status":"passed"}
        r = requests.put(url=exl_url, params=content,headers=self.header,json={'no':'1','status':'passed'})
        self.assertIn(r.status_code,{200})
        self.result = self.get_and_post('get_ad_materia_subtitle_list')[1]