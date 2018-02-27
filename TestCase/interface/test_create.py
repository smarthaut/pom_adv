#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 13:55
# @Author  : huanghe
# @Site    : 
# @File    : test_create.py
# @Software: PyCharm
import os
import sys
import unittest

import requests

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from baselib.db import mongo_db
import json


class CreateTest(unittest.TestCase):


    def setUp(self):
        headers = {
            'Accept': 'application/json',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json'
        }
        self.base_url = 'http://10.50.3.88:8090/aquapaas/sdp/ticket/external'
        self.header = headers
        db = mongo_db.DB()
        self.collection = db.getConnection(table_name='aquapaas',connection_name='svod')

    def tearDown(self):
        print(self.result)

    def get_and_post(self,type):
        content = self.collection.find({'type':type})[0]['content']
        r = requests.post(url=self.base_url, data=json.dumps(content), headers=self.header)
        self.result = r.json()
        return self.result

    #def get_and_update_timestamp(self):
       # now = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        #self.collection.



    def test_create_asset_ticket(self):
        # note : test for create asset ticket
        #content = self.collection.find({'type':'create_ticket_ex_asset'})[0]['content']
        #r = requests.post(url=self.base_url, data=json.dumps(content), headers=self.header)
        self.result = self.get_and_post('create_ticket_ex_asset')
        #self.result = r.json()
        self.assertIn(self.result['status'],{200,409})
        #self.assertEqual(self.result['status'],200)

    def test_create_asset_ticket_with_erroruser(self):
        # note : test for create ticket with error user
        self.result = self.get_and_post('create_ticket_with_erroruser')
        self.assertEqual(self.result['code'],'ticket.user_not_found')

    def test_create_asset_ticket_with_app(self):
        #note : test for create ticket with app 认证，在QA环境中没有意义
        self.result = self.get_and_post('create_assetticket_with_app')
        self.assertIn(self.result['status'], {200, 409})

    def test_create_asset_ticket_with_channel(self):
        #note : test for create ticket with channel 认证，在QA的环境中没有意义
        self.result = self.get_and_post('create_assetticket_with_channel')
        self.assertIn(self.result['status'], {200, 409})

    def test_create_bundle_ticket(self):
        #note : test for create bundle ticket
        self.result = self.get_and_post('create_bundleticket')
        self.assertIn(self.result['status'], {200, 409})

    if __name__ == '__main':
        unittest.main()