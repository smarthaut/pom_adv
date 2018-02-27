#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 13:03
# @Author  : huanghe
# @Site    : 
# @File    : test_selenium.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from seleniumlib.base_page import Basepage
from zq_lib.AquaPassAdv.login_page import LoginPage
import time
from time import sleep

driver = webdriver.Firefox()
driver.get('http://10.50.4.115:8080/paasadv/')
time.sleep(3)
driver01 = Basepage(driver)
driver01.type(selector="id=>login_dialog_input_user_mail",text='adv_admin')
driver01.type(selector="id=>login_dialog_input_user_pwd",text='123')
driver01.click(selector="id=>login_dialog_login_button")
driver.find_element_by_xpath('//div[@id="main_page_menu_guanggaowei"]/div[@class="main_expandable_back"]').click()
driver.find_element_by_css_selector('div#adPos_adKind_tuwen').click()
driver.find_element_by_id('adPos_addPosition').click()
sleep(0.3)
driver.find_element_by_css_selector('input#adPos_dialog_ne_id').send_keys('123456')
