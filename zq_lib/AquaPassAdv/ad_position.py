#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
from seleniumlib.base_page import Basepage

class AdPostion(Basepage):
    def rec_picture_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"图文"按钮.')
        return self.find_element('css_selector=>div#adPos_adKind_tuwen')
    
    def rec_video_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"贴片"按钮.')
        return self.find_element('css_selector=>div#adPos_adKind_tiepian')
         
    def click_picture_btn(self):
        self.rec_picture_btn().click()
        return Picture(self.driver)

    def click_video_btn(self):
        self.rec_video_btn().click()
        return Video(self.driver)
    
  
class Picture(Basepage):
    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"新建广告位"按钮.')
        return self.find_element('css_selector=>div.panel_page_button_text')
    
    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"新建广告位 "按钮.')
        self.click_ele(self.rec_create_btn())
        return CreateAdPostionForPicture(self.driver)
    
    def rec_total_page_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"共几页"input.')
        return self.find_element('xpath=>//td[@styledlistfunc="totPage"]')
    
    @property    
    def rec_total_page(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'获取"总共有几页"的值.')
        
        page_number = self.rec_total_page_btn().text
        return page_number
        #return self.driver.find_element_by_xpath('//div[@id="adPos_position_list"]/table/tfoot/tr/td/table/tbody/tr/td[8]').text
    
    def rec_specific_page_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"转到第几页"input.')
        return self.driver.find_element_by_xpath('//div[@id="content_container"]/div[@class="panel_container"]/div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tfoot/tr/td/table/tbody/tr/td[2]/input')
    
    
    def rec_next_page_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"NextPage"按钮.')
        return self.driver.find_element_by_xpath('//div[@id="content_container"]/div[@class="panel_container"]/div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tfoot/tr/td/table/tbody/tr/td[13]')
    
    def click_next_page_btn(self): 
        self.rec_next_page_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"NextPage"按钮.')       
        return None
    """
                    当前环境，添加广告位后会，添加到最后一页，需要报bug
    """
    def rec_new_create_ad_info(self):       
        self.logger = logging.getLogger(__name__)
        picture_info=[]
        self.logger.debug(u'获取"最后一页的广告位信息".')   
        trs = self.driver.find_elements_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr')
        num = 0
        for tr in trs:
            id = tr.find_element_by_xpath('.//td[1]').text
            self.logger.debug(u'id为  %s.'  % id)  
            if id == "":
                break
            num = num + 1
        self.logger.debug(u'num为  %s".'  % num)  
        ad_id =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[1]' % num ).text
        self.logger.debug(u'新创广告位id为  %s".'  % ad_id)  
        picture_info.append( ad_id )
        
        ad_name =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[2]' % num ).text
        picture_info.append( ad_name )
        
        ad_size =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[3]' % num ).text
        picture_info.append( ad_size )
          
        ad_creater =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[4]' % num ).text
        picture_info.append( ad_creater ) 
        
        ad_modify_time =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[5]' % num ).text
        picture_info.append( ad_modify_time ) 
        
        ad_number =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[6]' % num ).text
        picture_info.append( ad_number ) 
         
        return picture_info  
        
    
class Video(Basepage):
    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"新建广告位"按钮.')
        return  self.driver.find_element_by_id('adPos_addPosition')
        #return self.driver.find_element_by_css_selector('div.panel_page_button_text')

    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"新建广告位 "按钮.')
        self.rec_create_btn().click()
        return CreateAdPostionForVideo(self.driver)
    
    def rec_new_create_material_info(self):       
        self.logger = logging.getLogger(__name__)
        material_info=[]
        self.logger.debug(u'获取"最后一页的广告位信息".')   
        trs = self.driver.find_elements_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr')
        num = 0
        for tr in trs:
            id = tr.find_element_by_xpath('.//td[1]').text
            self.logger.debug(u'id为  %s.'  % id)  
            if id == "":
                break
            num = num + 1
        self.logger.debug(u'num为  %s".'  % num)  
        ad_id =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[1]' % num ).text
        self.logger.debug(u'新创广告位id为  %s".'  % ad_id)  
        material_info.append( ad_id )
        
        ad_author =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[2]' % num ).text
        material_info.append( ad_author )
        
        movie_number =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[3]' % num ).text
        material_info.append(  movie_number ) 
        
        ad_modify_time =  self.driver.find_element_by_xpath('//div[@class="panel_page_list_container"]/div[@id="adPos_position_list"]/table/tbody/tr[%s]/td[4]' % num ).text
        material_info.append( ad_modify_time ) 
         
        return material_info 
    
    
class CreateAdPostionForPicture(Basepage):
    def receive_ad_position_id_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"广告位ID"input.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_id')
    
    def receive_ad_position_name_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"广告位名称"input.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_name')
    
    def receive_size_width_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的宽"input.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_size_width')
    
    def receive_size_height_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的高 "按钮.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_size_height')
       
    def receive_ad_size_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"广告数量"按钮.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_count')
    
    def receive_create_ad_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"新建 "按钮.')
        return self.driver.find_element_by_css_selector('div#adPos_dialog_ne_submit')
    
    
    def receive_match_down_menu(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"适配建议"下拉控件.')
        return self.driver.find_element_by_xpath('//div[@id="adPos_dialog_ne_adapt_selector"]/div[@class="styled-selector-dropicon"]/div[@class="styled-selector-down-arrow"]')
    
    def _click_match_down_menu(self):
        self.receive_match_down_menu().click()
        return self.driver.find_element_by_xpath('//div[@class="panel_dialog_block"]/div[@id="adPos_dialog_ne_adapt_selector"]/div[@class="styled-selector-dropbox"]/table')
    
    
    def select_match_suggest(self,text):
        down_table = self._click_match_down_menu()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u"点击'%s'" % text)
        down_table.find_element_by_xpath('//tbody/tr/td[text()="%s"]' % text).click()
        return None    
    
    def receive_default_ad_down_menu(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"默认广告"下拉控件.')
        return self.driver.find_element_by_xpath('//div[@id="adPos_dialog_ne_dfAd_selector"]/div[@class="styled-selector-dropicon"]/div[@class="styled-selector-down-arrow"]')
    
    def _click_default_ad_down_menu(self):
        self.receive_default_ad_down_menu().click()
        return self.driver.find_element_by_xpath('//div[@id="adPos_dialog_ne_dfAd_selector"]/div[@class="styled-selector-dropbox"]/table')
    
    def select_default_ad(self,text):
        down_table = self._click_default_ad_down_menu()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u"点击'%s'" % text)
        down_table.find_element_by_xpath('//tbody/tr/td[text()="%s"]' % text).click()
        return None
    
    def receive_start_ad_checkbox(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"开机广告"checkbox.')
        return self.driver.find_element_by_css_selector('input#adPos_is_starting_up')
      
    def slect_start_ad_checkbox(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'选中"开机广告"checkbox.')
        checkbox = self.receive_start_ad_checkbox()
        if checkbox.get_attribute('value')=='1':
            checkbox.click() 
        return None
    
    def rec_new_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到新建广告位页面中"新建"按钮.')
        return self.driver.find_element_by_css_selector('div#adPos_dialog_ne_submit')    
    
    def rec_cancel_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到新建广告位页面中"取消"按钮.')
        return self.driver.find_element_by_css_selector('div#adPos_dialog_ne_cancel')    
    
    def click_new_create_btn(self): 
        self.logger = logging.getLogger(__name__)
        self.rec_new_create_btn().click()   
        self.logger.debug(u'点击新建广告位页面中"新建"按钮.') 
        #return Picture(self.driver)
        return None
    
    def click_cancel_btn(self): 
        self.rec_new_create_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击新建广告位页面中"取消"按钮.')       
        return Picture(self.driver)
       
class CreateAdPostionForVideo(Basepage):
    def receive_ad_position_id_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"广告位ID"input.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_id')
    
    def receive_ad_position_name_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"广告位名称"input.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_name')
    
    def receive_size_width_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的宽"input.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_size_width')
    
    def receive_size_height_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的高 "按钮.')
        return self.driver.find_element_by_css_selector('input#adPos_dialog_ne_size_height')
    
    
 
    
    def receive_default_ad_down_menu(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"默认广告"下拉控件.')
        return self.driver.find_element_by_xpath('//div[@class="panel_dialog_block"]/div[@id="adPos_dialog_ne_dfAd_selector"]/div[@class="styled-selector-dropicon"]/div[@class="styled-selector-down-arrow"]')
    
    def _click_default_ad_down_menu(self):
        self.receive_default_ad_down_menu().click()
        return self.driver.find_element_by_xpath('//div[@id="adPos_dialog_ne_dfAd_selector"]/div[@class="styled-selector-dropbox"]/table')
    
    def select_default_ad(self,text):
        down_table = self._click_default_ad_down_menu()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u"点击'%s'" % text)
        down_table.find_element_by_xpath('//tbody/tr/td[text()="%s"]' % text).click()
        return None
    
    
    def receive_add_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加"按钮.')
        return self.driver.find_element_by_css_selector('div#adPos_dialog_ne_patch_add')
    
    def click_add_btn(self): 
        self.receive_add_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"添加"按钮.')       
        return None
    def receive_time_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"时长"input.')
        return self.driver.find_element_by_xpath('//div[@class="adPos_dialog_ne_patch_content"]/div[@class="adPos_dialog_ne_patch_inputs_column"]/div[last()]/div[2]/input')
    
    def receive_mandatory_time_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"强制时长"input.')
        return self.driver.find_element_by_xpath('//div[@class="adPos_dialog_ne_patch_content"]/div[@class="adPos_dialog_ne_patch_inputs_column"]/div[last()]/div[4]/input')
    
    def receive_relative_deviation_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"相对偏移"input.')
        return self.driver.find_element_by_xpath('//div[@class="adPos_dialog_ne_patch_content"]/div[@class="adPos_dialog_ne_patch_inputs_column"]/div[last()]/div[6]/input')
    
    
    def rec_new_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到新建广告位页面中"新建"按钮.')
        return self.driver.find_element_by_css_selector('div#adPos_dialog_ne_submit')    
    
    def rec_cancel_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到新建广告位页面中"取消"按钮.')
        return self.driver.find_element_by_css_selector('div#adPos_dialog_ne_cancel')    
    
    def click_new_create_btn(self): 
        self.rec_new_create_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击新建广告位页面中"新建"按钮.')       
        return Video(self.driver)
    
    def click_cancel_btn(self): 
        self.rec_new_create_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击新建广告位页面中"取消"按钮.')       
        return Video(self.driver)