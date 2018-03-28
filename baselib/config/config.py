#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 14:18
# @Author  : huanghe
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os
from baselib.config.file_reader import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')

class Config():
    def __init__(self,config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self,element,index=0):
        return self.config[index].get(element)

if __name__ =='__main__':
    a = Config()
    print(a.get('URL'))