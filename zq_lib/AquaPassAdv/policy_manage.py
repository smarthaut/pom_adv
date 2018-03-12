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
        return Po(self.driver)

    def click_policy_viceo_btn(self):
        self.rec_policy_video_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击贴片按钮')
        return Po(self.driver)

    def click_policy_word(self):
        self.rec_policy_word_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击字幕按钮')
        return Po(self.driver)

class Po(Basepage):

    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"新建"按钮.')
        return self.find_element('id=>policy_add_btn')

    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"新建 "按钮.')
        self.rec_create_btn().click()
        return CreatePolicy(self.driver)

class CreatePolicy(Basepage):
    def rec_policy_name(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"策略名称"input.')
        return self.find_element('id=>policy_name')

    def rec_policy_priority(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"策略优先级"input.')
        return self.find_element('id=>policy_priority')
    def select_weight(self):
        self.logger = logging.getLogger(__name__)
        #self.logger.debug(u"点击'%s'" % text)
        self.driver.find_element_by_xpath(
            '//div[@id="policy_weight"]/div[@class="select-status select-box"]/div').click()

        self.driver.find_element_by_xpath('//div[@id="policy_weight"]/div[@class="select-status select-box"]/ul/li[30]').click()

        #num = int(text)
        #num = 30
        #if num in range(1,100):
            #self.driver.find_element_by_xpath('//div[@id="policy_weight"]/div[@class="select-status select-box"]/ul/li[30]').click()
        #else:
            #self.logger.error(u"策略权重不合法！")
        #return None
    #生效时间
    def rec_validtime_begin(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"生效时间"input.')
        return self.find_element('id=>validtime_date-datepicker-input')
    #失效时间
    def rec_validtime_end(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"失效时间"input.')
        return self.find_element('id=>invalidtime_date-datepicker-input')
    #频道标签
    def rec_channel_tag(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"频道标签".')
        return self.find_element('xpath=>//div[@id="tag_type"]/div[@class="select-status select-box"]/ul/li[1]')
    #栏目标签
    def rec_category_tag(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"栏目标签".')
        return self.find_element('xpath=>//div[@id="tag_type"]/div[@class="select-status select-box"]/ul/li[2]')

        # 频道标签
    def rec_area_tag(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"区域标签".')
        return self.find_element('xpath=>//div[@id="tag_type"]/div[@class="select-status select-box"]/ul/li[3]')

    #本次以频道标签为例
    def click_channel_tag(self):
        self.rec_channel_tag().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'选择"频道标签".')
    #选择具体的频道
    def rec_choose_channel_tag(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"频道标签选择".')
        return self.find_element('id=>policy_channel_choose')
    #点击标签选择
    def choose_channel_tag(self):
        self.rec_choose_channel_tag().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"频道标签选择".')
        return  ChooseTable(self.driver)
    #点击绑定广告位--选择
    def choose_ad_position(self):
        ele = self.find_element('id=>policy_adv_choose')
        ele.click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"绑定广告位--选择".')
        return ChooseTable(self.driver)
    #找到绑定素材组
    def rec_policy_bind_elgroup(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"绑定素材组".')
        return self.find_element('id=>policy_bind_elgroup')
    #找到绑定素材
    def rec_policy_bind_el(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"绑定素材".')
        return self.find_element('id=>policy_bind_el')
    #点击绑定素材组
    def click_policy_bind_elgroup(self):
        self.rec_policy_bind_elgroup().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"绑定素材组".')
    #点击绑定素材
    def click_policy_bind_el(self):
        self.rec_policy_bind_el().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"绑定素材".')
    #点击绑定素材（组）--选择
    def choose_bind_el(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"绑定素材(组)--选择".')
        self.find_element('id=>policy_sucai_choose').click()
        return ChooseTable(self.driver)
    def rec_canael_edit_dialog_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"取消"按钮.')
        return self.find_element('xpath=>//div[@id="popup-dialog-dialog"]/div/div[3]/div[4]')
    #找到确定按钮
    def rec_confirm_edit_dialog_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确定"按钮.')
        return self.find_element('xpath=>//div[@id="popup-dialog-dialog"]/div/div[3]/div[5]')
    #点击取消按钮
    def click_cancel_edit_dialog_btn(self):
        self.rec_canael_edit_dialog_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"取消"按钮.')
        return Po(self.driver)

    # 点击取消按钮
    def click_confirm_edit_dialog_btn(self):
        self.rec_confirm_edit_dialog_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"确认"按钮.')
        return Po(self.driver)


class ChooseTable(Basepage):
    #均选择第一个
    def choose_view(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"选择".')
        self.find_element('xpath=>//div[@id="select_table"]/table/tbody/tr[1]/td[3]/div/span[1]').click()
    def choose_select(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"选择".')
        self.find_element('xpath=>//div[@id="select_table"]/table/tbody/tr[1]/td[3]/div/span[2]').click()
    #找到取消按钮
    def rec_canael_select_dialog_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"取消"按钮.')
        return self.find_element('xpath=>//div[@class="cancel_btn select_dialog_btn"]')
    #找到确定按钮
    def rec_confirm_select_dialog_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确定"按钮.')
        return self.find_element('xpath=>//div[@class="confirm_btn select_dialog_btn"]')
    #点击取消按钮
    def click_cancel_select_dialog_btn(self):
        self.rec_canael_select_dialog_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"取消"按钮.')
        return CreatePolicy(self.driver)

    # 点击确认按钮
    def click_confirm_select_dialog_btn(self):
        self.rec_confirm_select_dialog_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"确认"按钮.')
        return CreatePolicy(self.driver)






