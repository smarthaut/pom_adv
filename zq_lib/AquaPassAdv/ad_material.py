#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
# from seleniumlib.basepage import BasePage
from seleniumlib.base_page import Basepage


class AdMaterial(Basepage):
    def rec_material_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材"按钮.')
        return self.find_element('s=>div.main_expandable_back')

    def click_material_btn(self):
        self.rec_material_btn().click()
        return MPicture(self.driver)

    def rec_mpicture_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"图片"按钮.')
        return self.find_element('id=>sucai_menu_select_img')

    def rec_mvideo_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"视频"按钮.')
        return self.find_element('id=>sucai_menu_select_video')

    def rec_mword_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"字幕"按钮.')
        return self.find_element('id=>sucai_menu_select_subtitle')

    def click_mpicture_btn(self):
        self.rec_mpicture_btn().click()
        return MPicture(self.driver)

    def click_mvideo_btn(self):
        self.rec_mvideo_btn().click()
        return MVideo(self.driver)

    def click_mword_btn(self):
        self.rec_mword_btn().click()
        return MWord(self.driver)


class MPicture(Basepage):
    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加素材"按钮.')
        return self.find_element('xpath=>//div[@id="sucai_add_class_btn"]/span')

    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"添加素材 "按钮.')
        self.rec_create_btn().click()
        return CreateMaterialForPicture(self.driver)

    def rec_new_material_info_for_picture(self):
        self.logger = logging.getLogger(__name__)
        material_info = []
        self.logger.debug(u'获取"最后一页的素材信息".')
        trs = self.driver.find_elements_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr')
        num = 0
        for tr in trs:
            material_name = tr.find_element_by_xpath('.//td[1]').text
            self.logger.debug(u'素材名称为  %s.' % material_name)
            if material_name == "":
                break
            num = num + 1
        self.logger.debug(u'num为  %s".' % num)
        material_name = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[1]' % num).text
        self.logger.debug(u'素材名称为  %s".' % material_name)
        material_info.append(material_name)

        material_status = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[2]' % num).text
        material_info.append(material_status)

        material_author = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[3]' % num).text
        material_info.append(material_author)

        material_size = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[4]' % num).text
        material_info.append(material_size)
        return material_info


class CreateMaterialForPicture(Basepage):
    def receive_material_name_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材名称"input.')
        return self.find_element('s=>input#sucai_dialog_create_input_name_value')

    def receive_sucai_width_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的宽"input.')
        return self.find_element('s=>input#sucai_dialog_create_input_size_width')

    def receive_sucai_height_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的高 "按钮.')
        return self.find_element('s=>input#sucai_dialog_create_input_size_height')

    '''def select_weight(self):
        self.logger = logging.getLogger(__name__)
        text = 30
        if text in [10, 30, 50, 70, 100]:
            self.driver.find_element_by_xpath(
                '//div[@id="sucai_dialog_create_morenguanggaowei_select"]/div[@class="select-status select-box"]/ul/li[3]').click()
        else:
            self.logger.error(u"输入权重错误！")
        return None'''
    def select_weight(self):
        self.logger = logging.getLogger(__name__)
        return self.find_element('xpath=>//div[@id="sucai_dialog_create_morenguanggaowei_select"]/div/div')

    def select_num(self,text):
        self.logger = logging.getLogger(__name__)
        if text in [10,30,50,70,100]:
            self.select_weight().click()
            return self.find_element('xpath=>//div[@id="sucai_dialog_create_morenguanggaowei_select"]/div/ul/li[text()=%s]' %text)
        else:
            self.logger.error(u'输入权重错误')
            return self.find_element('xpath=>//div[@id="sucai_dialog_create_morenguanggaowei_select"]/div/div')
    def receive_material_select_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"浏览"按钮.')
        return self.find_element('id=>sucai_dialog_create_uploadfile_click')

    def click_upload(self):
        self.logger = logging.getLogger(__name__)
        self.receive_material_select_input().click()
        self.logger.debug(u'点击"浏览"按钮.')

    def receive_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确认"按钮.')
        return self.find_element(
            'xpath=>//div[@class="sucai_dialog_create_opition"]/div[@id="sucai_dialog_create_botton_click"]')

    def click_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.receive_confirm_btn().click()
        self.logger.debug(u'点击添加素材页面中"确认"按钮.')

    def receive_cancel_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确认"按钮.')
        return self.find_element('xpath=>//div[@class="sucai_dialog_create_opition"]/div[1]')

    def click_cancel_btn(self):
        self.receive_cancel_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击新建广告位页面中"取消"按钮.')
        return MPicture(self.driver)


class MVideo(Basepage):
    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加素材"按钮.')
        return self.find_element('xpath=>//div[@id="sucai_add_class_btn"]/span')

    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"添加素材 "按钮.')
        self.rec_create_btn().click()
        return CreateMaterialForVideo(self.driver)

    def rec_new_material_info_for_video(self):
        self.logger = logging.getLogger(__name__)
        material_info = []
        self.logger.debug(u'获取"最后一页的素材信息".')
        trs = self.driver.find_elements_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr')
        num = 0
        for tr in trs:
            material_name = tr.find_element_by_xpath('.//td[1]').text
            self.logger.debug(u'素材名称为  %s.' % material_name)
            if material_name == "":
                break
            num = num + 1
        self.logger.debug(u'num为  %s".' % num)
        material_name = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[1]' % num).text
        self.logger.debug(u'素材名称为  %s".' % material_name)
        material_info.append(material_name)

        material_status = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[2]' % num).text
        material_info.append(material_status)

        material_author = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[3]' % num).text
        material_info.append(material_author)

        material_size = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[4]' % num).text
        material_info.append(material_size)

        material_time = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[5]' % num).text
        material_info.append(material_time)

        material_weigh = self.driver.find_element_by_xpath(
            '//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[6]' % num).text
        material_info.append(material_weigh)

        return material_info


class CreateMaterialForVideo(Basepage):
    def receive_material_name_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材名称"input.')
        return self.find_element('s=>input#sucai_dialog_create_input_name_value')

    def receive_sucai_width_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的宽"input.')
        return self.find_element('s=>input#sucai_dialog_create_input_size_width')

    def receive_sucai_height_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的高 "input.')
        return self.find_element('s=>input#sucai_dialog_create_input_size_height')

    def receive_sucai_time_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材时长 "input.')
        return self.find_element(
            'xpath=>//div[@class="sucai_dialog_create_size"]/input[@id="sucai_dialog_create_input_time_value"]')

    def select_weight(self):
        self.logger = logging.getLogger(__name__)
        return self.find_element('xpath=>//div[@id="sucai_dialog_create_morenguanggaowei_select"]/div/div')

    def select_num(self,text):
        self.logger = logging.getLogger(__name__)
        if text in [10,30,50,70,100]:
            self.select_weight().click()
            return self.find_element('xpath=>//div[@id="sucai_dialog_create_morenguanggaowei_select"]/div/ul/li[text()=%s]' %text)
        else:
            self.logger.error(u'输入权重错误')
            return self.find_element('xpath=>//div[@id="sucai_dialog_create_morenguanggaowei_select"]/div/div')

    def receive_material_select_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"选择素材"input.')
        return self.find_element('id=>sucai_dialog_create_uploadfile_click')

    def click_upload(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"选择素材"input.')
        self.receive_material_select_input().click()

    def receive_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确认"按钮.')
        return self.driver.find_element_by_xpath(
            '//div[@class="sucai_dialog_create_opition"]/div[@id="sucai_dialog_create_botton_click"]')

    def click_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.receive_confirm_btn().click()
        self.logger.debug(u'点击添加素材页面中"确认"按钮.')
        return None

    def receive_cancel_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确认"按钮.')
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_opition"]/div[1]')

    def click_cancel_btn(self):
        self.receive_cancel_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击新建广告位页面中"取消"按钮.')
        return MVideo(self.driver)


class MWord(Basepage):
    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加素材"按钮.')
        return self.find_element('xpath=>//div[@id="sucai_add_class_btn"]/span')

    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"添加素材 "按钮.')
        self.rec_create_btn().click()
        return CreateMaterialForWord(self.driver)


class CreateMaterialForWord(Basepage):
    def receive_material_name_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材名称"input.')
        return self.find_element('id=>sucai_dialog_create_input_name_value')

    def receive_material_textarea_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"字幕内容"input')
        return self.find_element('id=>sucai_dialog_create_subtitle_content')

    def receive_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确认"按钮.')
        return self.driver.find_element_by_xpath(
            '//div[@class="sucai_dialog_create_opition"]/div[@id="sucai_dialog_create_botton_click"]')

    def click_confirm_btn(self):
        self.logger = logging.getLogger(__name__)
        self.receive_confirm_btn().click()
        self.logger.debug(u'点击添加素材页面中"确认"按钮.')
        return None

    def receive_cancel_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"确认"按钮.')
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_opition"]/div[1]')

    def click_cancel_btn(self):
        self.receive_cancel_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击新建广告位页面中"取消"按钮.')
        return MWord(self.driver)