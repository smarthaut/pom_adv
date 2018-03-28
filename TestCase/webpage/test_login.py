#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 14:30
# @Author  : huanghe
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
import unittest
import os, sys
from baselib.logging.pylogging import setup_logging
from seleniumlib.browser import Browser
from zq_lib.AquaPassAdv.login_page import LoginPage
from baselib.config.config import Config
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from time import sleep
from baselib.config.config import Config

setup_logging()
import time



class AquaPaasAdvTest(unittest.TestCase):
    def setUp(self):
        self.driver = Browser(timeout=60)
        login_page = LoginPage(self.driver)
        login_page.url = Config().get('URL')
        login_page.visit()
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(), text=Config().get('USER'))
        login_page.set_value(element=login_page.rec_passwd_input(), text=Config().get('PASSWORD'))
        login_page.click_login_btn()
        self.first_page = login_page.get_first_page()

    def tearDown(self):
        # ...
        self.driver.quit()
    def test_creat_mword_materia(self):
        now = time.strftime("%Y%m%d%H%M%S")
        # 进入广告页面
        sleep(2)
        self.first_page.rec_material_btn()
        self.ad_materia_page = self.first_page.click_material_btn()
        sleep(0.5)
        self.mword_page = self.ad_materia_page.click_mword_btn()
        sleep(2)
        self.create_mword_materia_page = self.mword_page.click_create_btn()
        self.create_mword_materia_page.set_value(self.create_mword_materia_page.receive_material_name_input()
                                                 ,text=(now + '字幕素材'))
        self.create_mword_materia_page.set_value(self.create_mword_materia_page.receive_material_textarea_input()
                                                 ,text=u'日前，从全省住房和城乡建设工作会议上获悉，今年起我省将实施棚户区改造三年攻坚计划，2018、2019年集中攻坚，2020年扫尾。今年我省棚户区改造开工建设23万套，省政府将与各市签订目标责任书，'
                                                       u'大力推进棚改开工任务落实，同时抓好往年棚改项目竣工入住')
        self.create_mword_materia_page.click_confirm_btn()
        self.ad_materia_page.get_windows_img()


if __name__ == '__main':
    unittest.main()
