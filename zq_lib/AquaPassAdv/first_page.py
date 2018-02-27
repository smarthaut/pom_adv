#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
#from seleniumlib.basepage import BasePage
from seleniumlib.base_page import Basepage
from zq_lib.AquaPassAdv.ad_position import AdPostion
from zq_lib.AquaPassAdv.ad_material import AdMaterial
from zq_lib.AquaPassAdv.material_group import MaterialGroup

class FirstPage(Basepage):
    def rec_ad_position_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"广告位"按钮.')
        return self.find_element('xpath=>//div[@id="main_page_menu_guanggaowei"]/div[@class="main_expandable_back"]')
    
    def rec_material_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材"按钮.')
        return self.find_element('xpath=>//div[@id="main_page_menu_sucai"]/div[@class="main_expandable_back"]')
    
    def rec_material_group_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材组"按钮.')
        return self.find_element('xpath=>//div[@id="main_page_menu_sucaizu"]/div[@class="main_expandable_back"]')

    def rec_policy_manage_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"策略管理"按钮.')
        return self.find_element('xpath=>//div[@id="main_page_menu_celueguanli"]/div[@class="main_expandable_back"]')
         
    def click_ad_position_btn(self):
        self.click_ele(self.rec_ad_position_btn())
        self.logger.debug(u'进入"广告"页面')
        return AdPostion(self.driver)

    def click_material_btn(self):
        self.rec_material_btn().click()
        self.logger.debug(u'进入"素材"页面.')
        return AdMaterial(self.driver)

    def click_material_group_btn(self):
        self.rec_material_group_btn().click()
        self.logger.debug(u'进入"素材组"页面.')
        return MaterialGroup(self.driver)

    def click_policy_manage_btn(self):
        self.rec_policy_manage_btn().click()
        self.logger.debug(u'进入"策略管理"页面.')

