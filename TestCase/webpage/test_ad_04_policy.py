#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 17:36
# @Author  : huanghe
# @Site    :
# @File    : test_ad_policy.py
# @Software: PyCharm
import unittest
import os, sys
from baselib.logging.pylogging import setup_logging
from seleniumlib.browser import Browser
from zq_lib.AquaPassAdv.login_page import LoginPage

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from time import sleep

setup_logging()
import time


class AquaPaasAdvTest(unittest.TestCase):
    def setUp(self):
        self.driver = Browser(timeout=60)
        login_page = LoginPage(self.driver)
        login_page.url = 'http://10.50.4.115:8080/paasadv/'
        login_page.visit()
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(), text="root")
        login_page.set_value(element=login_page.rec_passwd_input(), text="123")
        login_page.click_login_btn()
        self.first_page = login_page.get_first_page()

    def tearDown(self):
        # ...
        self.driver.quit()
        # 创建图片策略

    def test_create_policy_img(self):
        now = time.strftime("%Y%m%d%H%M%S")
        # 进入广告页面
        sleep(2)
        self.ad_policy_page = self.first_page.click_policy_manage_btn()
        sleep(0.5)
        self.create_policy_page = self.ad_policy_page.click_policy_picture_btn()
        self.create_policy_image_page = self.create_policy_page.click_create_btn()
        sleep(0.5)
        self.create_policy_image_page.set_value(self.create_policy_image_page.rec_policy_name()
                                                , text=(now + '图文策略'))
        self.create_policy_image_page.set_value(self.create_policy_image_page.rec_policy_priority()
                                                , text=10)
        self.create_policy_image_page.select_weight()

        sleep(0.5)
        self.create_policy_image_page.set_value(self.create_policy_image_page.rec_validtime_begin()
                                                , text='2016-03-01')
        self.create_policy_image_page.set_value(self.create_policy_image_page.rec_validtime_end()
                                                , text='2019-03-02')
        self.choose_tag_page = self.create_policy_image_page.choose_channel_tag()
        self.choose_tag_page.choose_select()
        self.choose_tag_page.click_confirm_select_dialog_btn()
        self.choose_position_page = self.create_policy_image_page.choose_ad_position()
        self.choose_position_page.choose_view()
        self.choose_position_page.click_confirm_select_dialog_btn()
        self.create_policy_image_page.click_policy_bind_el()
        self.choose_el_page = self.create_policy_image_page.choose_bind_el()
        self.choose_el_page.choose_select()
        self.choose_el_page.click_confirm_select_dialog_btn()
        self.create_policy_image_page.click_confirm_edit_dialog_btn()
        self.create_policy_page.get_windows_img()

        # 创建视频策略

    def test_create_policy_video(self):
        now = time.strftime("%Y%m%d%H%M%S")
        # 进入广告页面
        sleep(2)
        self.ad_policy_page = self.first_page.click_policy_manage_btn()
        sleep(0.5)
        self.create_policy_page = self.ad_policy_page.click_policy_viceo_btn()
        self.create_policy_video_page = self.create_policy_page.click_create_btn()
        sleep(0.5)
        self.create_policy_video_page.set_value(self.create_policy_video_page.rec_policy_name()
                                                , text=(now + '视频策略'))
        self.create_policy_video_page.set_value(self.create_policy_video_page.rec_policy_priority()
                                                , text=10)
        self.create_policy_video_page.select_weight()

        sleep(0.5)
        self.create_policy_video_page.set_value(self.create_policy_video_page.rec_validtime_begin()
                                                , text='2015-03-01')
        self.create_policy_video_page.set_value(self.create_policy_video_page.rec_validtime_end()
                                                , text='2017-03-01')
        self.choose_tag_page = self.create_policy_video_page.choose_channel_tag()
        self.choose_tag_page.choose_select()
        self.choose_tag_page.click_confirm_select_dialog_btn()
        self.choose_position_page = self.create_policy_video_page.choose_ad_position()
        self.choose_position_page.choose_view()
        self.choose_position_page.click_confirm_select_dialog_btn()
        self.create_policy_video_page.click_policy_bind_el()
        self.choose_el_page = self.create_policy_video_page.choose_bind_el()
        self.choose_el_page.choose_select()
        self.choose_el_page.click_confirm_select_dialog_btn()
        self.create_policy_video_page.click_confirm_edit_dialog_btn()
        self.create_policy_page.get_windows_img()
        # 创建字幕策略
    def test_create_policy_word(self):
        now = time.strftime("%Y%m%d%H%M%S")
        # 进入广告页面
        sleep(2)
        self.ad_policy_page = self.first_page.click_policy_manage_btn()
        sleep(0.5)
        self.create_policy_page = self.ad_policy_page.click_policy_word()
        self.create_policy_word_page = self.create_policy_page.click_create_btn()
        sleep(0.5)
        self.create_policy_word_page.set_value(self.create_policy_word_page.rec_policy_name()
                                               , text=(now + '字幕策略'))
        self.create_policy_word_page.set_value(self.create_policy_word_page.rec_policy_priority()
                                               , text=10)
        self.create_policy_word_page.select_weight()

        sleep(0.5)
        self.create_policy_word_page.set_value(self.create_policy_word_page.rec_validtime_begin()
                                               , text='2013-03-01')
        self.create_policy_word_page.set_value(self.create_policy_word_page.rec_validtime_end()
                                               , text='2014-03-01')
        self.choose_tag_page = self.create_policy_word_page.choose_channel_tag()
        self.choose_tag_page.choose_select()
        self.choose_tag_page.click_confirm_select_dialog_btn()
        self.choose_position_page = self.create_policy_word_page.choose_ad_position()
        self.choose_position_page.choose_view()
        self.choose_position_page.click_confirm_select_dialog_btn()
        self.create_policy_word_page.click_policy_bind_el()
        self.choose_el_page = self.create_policy_word_page.choose_bind_el()
        self.choose_el_page.choose_select()
        self.choose_el_page.click_confirm_select_dialog_btn()
        self.create_policy_word_page.click_confirm_edit_dialog_btn()
        self.create_policy_page.get_windows_img()


if __name__ == '__main':
    unittest.main()
