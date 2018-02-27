#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 14:27
# @Author  : huanghe
# @Site    : 
# @File    : policy_manage.py
# @Software: PyCharm
import logging
from seleniumlib.base_page import Basepage

class PolicyManage(Basepage):
    def rec_policy_picture_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"图文"按钮.')
        return self.driver.find_element_by_css_selector('div#adPos_adKind_tuwen')

    def rec_policy_video_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"贴片"按钮.')
        return self.driver.find_element_by_css_selector('div#adPos_adKind_tiepian')
