#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 15:26
# @Author  : huanghe
# @Site    :
# @File    : login_pag.py
# @Software: PyCharm
import logging
from seleniumlib.base_page import Basepage
from zq_lib.AquaPassAdv.first_page import FirstPage


class LoginPage(Basepage):
    def rec_user_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"登录用户名"输入input.')
        return self.find_element(selector='id=>login_dialog_input_user_mail')
        #return self.driver.find_element_by_id('login_dialog_input_user_mail')
        # return self.driver.find_element_by_css_selector('input#login_dialog_input_user_mail')

    def rec_passwd_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"密码"输入input.')
        return self.find_element(selector='id=>login_dialog_input_user_pwd')
        #return self.driver.find_element_by_id('login_dialog_input_user_pwd')

    def rec_rmb_user_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"记住用户名"按钮.')
        return self.find_element(selector='id=>login_dialog_rmb_user')
        #return self.driver.find_element_by_id('login_dialog_rmb_user')

    def rec_rmb_pwd_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"记住密码"按钮.')
        return self.find_element(selector='id=>login_dialog_rmb_pwd')
        #return self.driver.find_element_by_id('login_dialog_rmb_pwd')

    def rec_login_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"立即登录"按钮.')
        return self.find_element(selector='id=>login_dialog_login_button')
        #return self.driver.find_element_by_id('login_dialog_login_button')

    def click_login_btn(self):
        self.logger = logging.getLogger(__name__)
        self.click_sel(selector='id=>login_dialog_login_button')
        #self.rec_login_btn().click()
        self.logger.debug(u'点击"立即登录 "按钮.')
        #return FirstPage(self.driver)

    def get_first_page(self):
        return FirstPage(self.driver)
