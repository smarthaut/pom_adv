#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 14:44
# @Author  : huanghe
# @Site    : 
# @File    : run_tests.py
# @Software: PyCharm
import sys
import time

#sys.path.append('./interface')
#sys.path.append('./db_mongodb')
from baselib.htmltestrunner.HTMLTestRunner import HTMLTestRunner
import unittest

#test_dir = './TestCase/interface'
test_dir = './TestCase/webpage'
#
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Aquapaas WEB ADV Test Report',
                            description='Implementation Example with: '

                            )
    run = HTMLTestRunner()
    runner.run(discover)
    fp.close()