#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 13:47
# @Author  : huanghe
# @Site    : 
# @File    : test_batch_create.py
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
        self.base_url = 'http://10.50.3.88:8090/aquapaas/sdp/ticket/batchexternal'
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

    def test_batch_create_ticket(self):
        # note : test for batch create ticket
        self.result = self.get_and_post('batch_create_ticket')
        self.assertIn(self.result['status'], {200, 409})

    def test_batch_create_ticket_rollback(self):
        self.result= self.get_and_post('batch_create_ticket_rollback')
        self.assertIn(self.result['status'],{404,409})

    def test_bach_create_ticket_unrollback(self):
        self.result = self.get_and_post('batch_create_ticket_unrollback')
        self.assertIn(self.result['status'], {200})



if __name__ == '__main':
    unittest.main()
