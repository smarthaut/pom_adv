#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 14:30
# @Author  : huanghe
# @Site    :
# @File    : test_ad_materia_group.py
# @Software: PyCharm
import unittest
import os,sys
from baselib.logging.pylogging import setup_logging
from seleniumlib.browser import Browser
from zq_lib.AquaPassAdv.login_page import LoginPage
from baselib.config.config import Config
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from time import sleep
setup_logging()
import time

class AquaPaasAdvTest(unittest.TestCase):

    def setUp(self):
        self.driver = Browser(timeout=60)
        login_page = LoginPage(self.driver)
        login_page.url=Config().get('URL')
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(),text=Config().get('USER'))
        login_page.set_value(element=login_page.rec_passwd_input(),text=Config().get('PASSWORD'))
        login_page.click_login_btn()
        self.first_page = login_page.get_first_page()

    def tearDown(self):
        #...
        self.driver.quit()

#创建图片素材组
    def test_create_mgpicture_materia(self):
        now = time.strftime("%Y%m%d%H%M%S")
        #进入广告页面
        sleep(2)
        self.first_page.rec_material_btn()
        self.ad_materia_group_page = self.first_page.click_material_group_btn()
        sleep(0.5)
        self.mgpicture_page = self.ad_materia_group_page.click_mgpicture_btn()
        self.create_mpicture_materia_page = self.mgpicture_page.click_create_btn()
        sleep(0.5)
        self.create_mpicture_materia_page.set_value(self.create_mpicture_materia_page.receive_material_name_input()
                                                    ,text=(now + '图片素材组'))
        checkbox = self.create_mpicture_materia_page.receive_checkbox()
        checkbox[1].click()
        self.create_mpicture_materia_page.click_add_button()
        self.create_mpicture_materia_page.click_confirm_btn()
        self.mgpicture_page.get_windows_img()



#创建视频素材组
    def test_create_mvideo_materia(self):
        now = time.strftime("%Y%m%d%H%M%S")
        # 进入广告页面
        sleep(2)
        self.first_page.rec_material_btn()
        self.ad_materia_group_page = self.first_page.click_material_group_btn()
        sleep(0.5)
        self.mgword_page = self.ad_materia_group_page.click_mgvideo_btn()
        self.create_mgword_materia_page = self.mgword_page.click_create_btn()
        sleep(0.5)
        self.create_mgword_materia_page.set_value(self.create_mgword_materia_page.receive_material_name_input()
                                                  , text=(now + '视频素材组'))
        checkbox = self.create_mgword_materia_page.receive_checkbox()
        checkbox[1].click()
        self.create_mgword_materia_page.click_add_button()
        self.create_mgword_materia_page.click_confirm_btn()
        self.mgword_page.get_windows_img()


#创建字幕素材组
    def test_creat_mword_materia(self):
        now = time.strftime("%Y%m%d%H%M%S")
        # 进入广告页面
        sleep(2)
        self.first_page.rec_material_btn()
        self.ad_materia_group_page = self.first_page.click_material_group_btn()
        sleep(0.5)
        self.mgword_page = self.ad_materia_group_page.click_mgword_btn()
        self.create_mgword_materia_page = self.mgword_page.click_create_btn()
        sleep(0.5)
        self.create_mgword_materia_page.set_value(self.create_mgword_materia_page.receive_material_name_input()
                                                  , text=(now + '字幕素材组'))
        checkbox = self.create_mgword_materia_page.receive_checkbox()
        checkbox[1].click()
        self.create_mgword_materia_page.click_add_button()
        self.create_mgword_materia_page.click_confirm_btn()
        self.mgword_page.get_windows_img()



    if __name__ == '__main':
        unittest.main()