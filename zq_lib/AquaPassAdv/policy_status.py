#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 13:06
# @Author  : huanghe
# @Site    : 
# @File    : policy_status.py
# @Software: PyCharm
import logging
from seleniumlib.base_page import Basepage
from zq_lib.AquaPassAdv.policy_manage import CreatePolicy

class PolicyStatus(Basepage):
    def rec_policy_picture_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"图文"按钮.')
        return self.find_element('id=>policy_img')

    def rec_policy_video_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"贴片"按钮.')
        return self.find_element('id=>policy_video')

    def rec_policy_word_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"字幕"按钮.')
        return  self.find_element('id=>policy_txt')

    def click_policy_picture_btn(self):
        self.rec_policy_picture_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击图文按钮')
        return PS(self.driver)

    def click_policy_viceo_btn(self):
        self.rec_policy_video_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击贴片按钮')
        return PS(self.driver)

    def click_policy_word(self):
        self.rec_policy_word_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击字幕按钮')
        return PS(self.driver)

class PS(Basepage):



    def rec_policy_firstaudit_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"初审"按钮.')
        return self.find_element('id=>policy_firstAudit')

    def rec_policy_secondaudit_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"终审"按钮.')
        return self.find_element('id=>policy_secondAudit')

    def rec_policy_policy_enadle_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"启用"按钮.')
        return self.find_element('id=>policy_enable')

    def rec_policy_policy_disadble_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"禁用"按钮.')
        return self.find_element('id=>policy_disable')


    def click_first_audit(self):
        self.rec_policy_firstaudit_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击初审按钮')
        return Paas(self.driver)

    def click_second_audit(self):
        self.rec_policy_secondaudit_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击终审按钮')
        return Paas(self.driver)

    def click_policy_enable(self):
        self.rec_policy_policy_enadle_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击启用按钮')
        return Paas(self.driver)

    def click_policy_disable(self):
        self.rec_policy_policy_disadble_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击禁用按钮')
        return Paas(self.driver)

class Paas(Basepage):
    def rec_view_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"查看"按钮.')
        return self.find_element('xpath=>//div[@id="adPolicyAuditTable"]/table/tbody/tr[1]/td[10]/span[1]')

    def rec_no_pass_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"否决"按钮.')
        return self.find_element('xpath=>//div[@id="adPolicyAuditTable"]/table/tbody/tr[1]/td[10]/span[2]')

    def rec_pass_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到通过按钮')
        return self.find_element('xpath=>//div[@id="adPolicyAuditTable"]/table/tbody/tr[1]/td[10]/span[3]')

    def click_view_btn(self):
        self.logger = logging.getLogger(__name__)
        self.rec_view_btn().click()
        self.logger.debug(u'点击"查看"按钮.')
        return CreatePolicy(self.driver)

    def click_no_pass(self):
        self.logger = logging.getLogger(__name__)
        self.rec_no_pass_btn().click()
        self.logger.debug(u'点击禁用按钮')
        return Reason(self.driver)

    def click_pass(self):
        self.logger = logging.getLogger(__name__)
        self.rec_pass_btn().click()
        self.logger.debug(u'点击通过按钮')
        return Pass(self.driver)

class Pass(Basepage):
    def rec_cancel_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"关闭"按钮.')
        return self.find_element("s=>div.auditDialogCancelBtn")

    def rec_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确定"按钮.')
        return self.find_element('s=>div.auditDialogConfirmBtn')

    def click_cancel_btn(self):
        self.rec_cancel_btn().click()
        self.logger.debug(u'点击取消按钮')
        return PS(self.driver)

    def click_confirm_btn(self):
        self.rec_confirm_btn().click()
        self.logger.debug(u'点击确定按钮')
        return PS(self.driver)

class Reason(Basepage):
    ...