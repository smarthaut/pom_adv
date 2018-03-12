#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
from seleniumlib.base_page import Basepage


class MaterialGroup(Basepage):
    def rec_mgpicture_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"图片"按钮.')
        return self.find_element('id=>sucaizu_menu_select_img')

    def rec_mgvideo_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"视频"按钮.')
        return self.find_element('id=>sucaizu_menu_select_video')

    def rec_mgword_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"字幕"按钮.')
        return self.find_element('id=>sucaizu_menu_select_subtitle')

    def click_mgpicture_btn(self):
        self.rec_mgpicture_btn().click()
        return Mg(self.driver)

    def click_mgvideo_btn(self):
        self.rec_mgvideo_btn().click()
        return Mg(self.driver)

    def click_mgword_btn(self):
        self.rec_mgword_btn().click()
        return Mg(self.driver)


class Mg(Basepage):
    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加素材组"按钮.')
        return self.find_element('id=>sucaizu_add_class_btn')

    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"添加素材组 "按钮.')
        self.rec_create_btn().click()
        return CreateMaterialGroup(self.driver)


class CreateMaterialGroup(Basepage):
    def receive_material_name_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材组名称"input.')
        return self.find_element('s=>input#sucai_dialog_create_input_sucaizuname_value')

    def receive_query_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"查询"按钮.')
        return self.find_element(
            'xpath=>//div[@id="sucai_list_search_botton" and @class="sucai_list_search_botton_div"]')

    def receive_single_add_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加"按钮.')
        return self.find_element(
            'xpath=>//div[@class="sucai_dialog_create_move_sucai_two"]/div[@id="sucai_dialog_create_move_add"]')

    def receive_all_add_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加全部"按钮.')
        return self.find_element(
            'xpath=>//div[@class="sucai_dialog_create_move_sucai_two"]/div[@id="sucai_dialog_create_move_addall"]')

    def receive_checkbox(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到全部的checkbox')
        return self.driver.find_elements_by_name('styled-flow-list-body-item')

    def receive_single_delete_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"删除"按钮.')
        return self.find_element(
            'xpath=>//div[@class="sucai_dialog_create_move_sucai_two"]/div[@id="sucai_dialog_create_move_delete"]')

    def receive_all_delete_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"全部删除"按钮.')
        return self.find_element('id=>sucai_dialog_create_move_deleteall')

    def receive_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确认"按钮.')
        return self.find_element('id=>sucai_dialog_create_botton_click')

    def click_add_button(self):
        if self.receive_single_add_button():
            self.logger = logging.getLogger(__name__)
            self.logger.debug(u'点击添加按钮')
            self.receive_single_add_button().click()
        else:
            ...

    def click_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.receive_confirm_btn().click()
        self.logger.debug(u'点击新建素材组页面中"确认"按钮.')
        return None

    def receive_cancel_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"取消"按钮.')
        return self.find_element(
            'xpath=>//div[@class="sucai_dialog_create_opition"]/div[@class="option_bottom popup_dialog_clear"]')

    def click_cancel_btn(self):
        self.receive_cancel_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击新建素材组页面中"取消"按钮.')
        return Mg(self.driver)


