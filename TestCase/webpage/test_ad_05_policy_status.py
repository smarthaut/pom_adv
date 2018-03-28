#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 13:02
# @Author  : huanghe
# @Site    :
# @File    : test_ad_policy_status.py
# @Software: PyCharm
import unittest
import os, sys
from baselib.logging.pylogging import setup_logging
from seleniumlib.browser import Browser
from baselib.config.config import Config
from zq_lib.AquaPassAdv.login_page import LoginPage

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from time import sleep

setup_logging()



class AquaPaasAdvTest(unittest.TestCase):
    def setUp(self):
        self.driver = Browser(timeout=60)
        login_page = LoginPage(self.driver)
        login_page.url = Config().get('URL')
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(),text=Config().get('USER'))
        login_page.set_value(element=login_page.rec_passwd_input(),text=Config().get('PASSWORD'))
        login_page.click_login_btn()
        self.first_page = login_page.get_first_page()

    def tearDown(self):
        # ...
        self.driver.quit()

    def test_img_policy_status(self):
        # 进入策略审核页面
        sleep(2)
        self.ad_policy_status_page = self.first_page.click_policy_status_btn()
        self.img_policy_page = self.ad_policy_status_page.click_policy_picture_btn()
        self.policy_first_page = self.img_policy_page.click_first_audit()
        self.second_page = self.policy_first_page.click_pass().click_confirm_btn()
        self.second_page.click_second_audit().click_pass().click_confirm_btn()
        self.img_policy_page.get_windows_img()

    def test_videp_policy_status(self):
        # 进入策略审核页面
        sleep(2)
        self.ad_policy_status_page = self.first_page.click_policy_status_btn()
        self.img_policy_page = self.ad_policy_status_page.click_policy_viceo_btn()
        self.policy_first_page = self.img_policy_page.click_first_audit()
        self.second_page = self.policy_first_page.click_pass().click_confirm_btn()
        self.second_page.click_second_audit().click_pass().click_confirm_btn()
        self.img_policy_page.get_windows_img()

    def test_word_policy_status(self):
        # 进入策略审核页面
        sleep(2)
        self.ad_policy_status_page = self.first_page.click_policy_status_btn()
        self.img_policy_page = self.ad_policy_status_page.click_policy_word()
        self.policy_first_page = self.img_policy_page.click_first_audit()
        self.second_page = self.policy_first_page.click_pass().click_confirm_btn()
        self.second_page.click_second_audit().click_pass().click_confirm_btn()
        self.img_policy_page.get_windows_img()

if __name__ == '__main':
    unittest.main()
