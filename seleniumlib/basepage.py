#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 10:46
# @Author  : huanghe
# @Site    : 
# @File    : basepage.py
# @Software: PyCharm
import time
import os
import logging
from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    url = None

    def __init__(self,driver):
        self.driver = driver

    def title(self):
        return self.driver.title

    def get_url(self):
        return self.url

    def fill_form_by(self, finder, selector, value, wait_time=2, poll_frequency=0.5):
        elem = self.find_by(finder, selector, wait_time, poll_frequency)[0]
        elem.clear()
        elem.send_keys(value)

    def visit(self):
        self.driver.get(self.url)

    @staticmethod
    def find_by(finder, selector, wait_time=2, poll_frequency=0.5):
        elements = None
        end_time = time.time() + wait_time
        while time.time() <= end_time:
            try:
                elements = finder(selector)
                if not isinstance(elements, list):
                    elements = [elements]
            except NoSuchElementException:
                pass
            if elements:
                return elements
            time.sleep(poll_frequency)
        return None

    @staticmethod
    def set_value(element, value):
        if element.get_attribute('type') != 'file':
            element.clear()
        element.send_keys(value)

