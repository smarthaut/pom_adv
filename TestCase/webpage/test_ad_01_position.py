#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 16:45
# @Author  : huanghe
# @Site    :
# @File    : test_ad_position.py
# @Software: PyCharm
import unittest
import os,sys
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
        login_page.url='http://10.50.4.115:8080/paasadv/'
        login_page.visit()
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(),text="root")
        login_page.set_value(element=login_page.rec_passwd_input(),text="123")
        login_page.click_login_btn()
        self.first_page = login_page.get_first_page()

    def tearDown(self):
        ...
        self.driver.quit()


    def test_create_tiepian_ad_position(self):
        now = time.strftime("%Y%m%d%H%M%S")
        #进入广告页面
        sleep(2)
        self.first_page.rec_ad_position_btn()
        self.ad_position_page = self.first_page.click_ad_position_btn()
        sleep(0.5)
        self.ad_position_page.rec_video_btn()
        self.video_page = self.ad_position_page.click_video_btn()
        self.video_page.rec_create_btn()
        self.create_ad_postion_for_video = self.video_page.click_create_btn()
        sleep(0.5)
        self.create_ad_postion_for_video.set_value(self.create_ad_postion_for_video.receive_ad_position_id_input(),now)
        self.create_ad_postion_for_video.set_value(self.create_ad_postion_for_video.receive_ad_position_name_input(), text=(now+'贴片广告位'))
        self.create_ad_postion_for_video.set_value(self.create_ad_postion_for_video.receive_size_width_input(), "749")
        self.create_ad_postion_for_video.set_value(self.create_ad_postion_for_video.receive_size_height_input(), "477")
        self.create_ad_postion_for_video.set_value(self.create_ad_postion_for_video.receive_time_input(),'20')
        self.create_ad_postion_for_video.set_value(self.create_ad_postion_for_video.receive_mandatory_time_input(),'20')
        self.create_ad_postion_for_video.set_value(self.create_ad_postion_for_video.receive_relative_deviation_input(),'1/2')
        self.create_ad_postion_for_video.receive_add_btn()
        self.create_ad_postion_for_video.click_add_btn()
        self.create_ad_postion_for_video.select_default_ad(u'默认广告')
        self.create_ad_postion_for_video.click_new_create_btn()
        self.create_ad_postion_for_video.get_windows_img()

    def test_create_tuwen_ad_position(self):
        now = time.strftime("%Y%m%d%H%M%S")
        #进入广告页面
        sleep(2)
        self.adposition_page = self.first_page.click_ad_position_btn()
        sleep(0.5)
        self.picture_page = self.adposition_page.click_picture_btn()
        sleep(0.5)
        self.create_ad_postion_for_picture = self.picture_page.click_create_btn()
        self.create_ad_postion_for_picture.set_value(self.create_ad_postion_for_picture.receive_ad_position_id_input(), now)
        self.create_ad_postion_for_picture.set_value(self.create_ad_postion_for_picture.receive_ad_position_name_input(), text=(now+'图文广告位'))
        self.create_ad_postion_for_picture.set_value(self.create_ad_postion_for_picture.receive_size_width_input(), "749")
        self.create_ad_postion_for_picture.set_value(self.create_ad_postion_for_picture.receive_size_height_input(), "477")
        self.create_ad_postion_for_picture.set_value(self.create_ad_postion_for_picture.receive_ad_size_input(), "1")
        self.create_ad_postion_for_picture.select_match_suggest(u'可以拉伸')
        self.create_ad_postion_for_picture.select_default_ad(u'默认广告')
        self.create_ad_postion_for_picture.click_new_create_btn()
        self.create_ad_postion_for_picture.get_windows_img()

    def test_create_zimu_ad_position(self):
        now = time.strftime("%Y%m%d%H%M%S")
        #进入广告页面
        sleep(3)
        self.first_page.rec_ad_position_btn()
        self.ad_position_page = self.first_page.click_ad_position_btn()
        sleep(0.5)
        self.ad_position_page.rec_word_btn()
        self.video_page = self.ad_position_page.click_word_btn()
        self.video_page.rec_create_btn()
        self.create_ad_postion_for_word = self.video_page.click_create_btn()
        sleep(0.5)
        self.create_ad_postion_for_word.click_upload()
        os.system('D:/auit/upload.exe "D:\\pictures\\011.jpg"')
        sleep(5)
        self.create_ad_postion_for_word.switch_alert()
        self.create_ad_postion_for_word.set_value(self.create_ad_postion_for_word.receive_ad_position_id_input(), now)
        self.create_ad_postion_for_word.set_value(self.create_ad_postion_for_word.receive_ad_position_name_input(), text=(now + '字幕广告位'))
        self.create_ad_postion_for_word.set_value(self.create_ad_postion_for_word.receive_ad_position_size_word(),'14')
        self.create_ad_postion_for_word.set_value(self.create_ad_postion_for_word.receive_ad_position_word_color(),'111FFF')
        self.create_ad_postion_for_word.set_value(self.create_ad_postion_for_word.receive_ad_position_picture_opacity(),'50')
        self.create_ad_postion_for_word.set_value(self.create_ad_postion_for_word.receive_ad_position_num_limit(),'20')
        self.create_ad_postion_for_word.set_value(self.create_ad_postion_for_word.receive_ad_position_move_interval(),'10')
        self.create_ad_postion_for_word.set_value(self.create_ad_postion_for_word.receive_ad_position_long_move(),'10')
        self.create_ad_postion_for_word.click_new_create_btn()
        self.create_ad_postion_for_word.get_windows_img()


    if __name__ == '__main':
        unittest.main()