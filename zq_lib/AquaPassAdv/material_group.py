#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
#from seleniumlib.basepage import BasePage
from seleniumlib.base_page import Basepage

class MaterialGroup(Basepage):
    def rec_mgpicture_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"图片"按钮.')
        return self.driver.find_element_by_xpath('//div[@id="content_container"]/div[@id="sucai_container"]/div[@class="sucai_head"]/div[@class="sucai_head_left"]/div[@class="sucai_head_center"]/ul/li[@id="sucai_menu_select_img"]')
    
    def rec_mgvideo_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"视频"按钮.')
        return self.driver.find_element_by_xpath('//div[@id="content_container"]/div[@id="sucai_container"]/div[@class="sucai_head"]/div[@class="sucai_head_left"]/div[@class="sucai_head_center"]/ul/li[@id="sucai_menu_select_video"]')
         
    def click_mgpicture_btn(self):
        self.rec_mgpicture_btn().click()
        return Mgpicture(self.driver)

    def click_mgvideo_btn(self):
        self.rec_mgvideo_btn().click()
        return Mgvideo(self.driver)
    
   
class Mgpicture(Basepage):
    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加素材组"按钮.')
        return self.driver.find_element_by_xpath('//div[@id="sucaizu_add_class_btn"]/span')

    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"添加素材组 "按钮.')
        self.rec_create_btn().click()
        return CreateMaterialGroupForPicture(self.driver)
    
    
    
    def rec_new_material_group_info_for_picture(self):
        self.logger = logging.getLogger(__name__)
        material_info=[]
        self.logger.debug(u'获取"最后一页的素材信息".')
        trs = self.driver.find_elements_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr')
        num = 0
        for tr in trs:
            material_name = tr.find_element_by_xpath('.//td[1]').text
            self.logger.debug(u'素材名称为  %s.'  % material_name)
            if material_name == "":
                break
            num = num + 1
        self.logger.debug(u'num为  %s".'  % num)
        material_name =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[1]' % num ).text
        self.logger.debug(u'素材名称为  %s".'  % material_name)
        material_info.append( material_name )
        
        material_status =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[2]' % num ).text
        material_info.append( material_status )
        
        material_author =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[3]' % num ).text
        material_info.append(  material_author ) 
        
        material_size =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[4]' % num ).text
        material_info.append( material_size ) 
        return material_info 
    
    
class CreateMaterialGroupForPicture(Basepage):
    def receive_material_name_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材组名称"input.')
        return self.driver.find_element_by_css_selector('input#sucai_dialog_create_input_sucaizuname_value')
    
    def receive_query_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"查询"按钮.')
        return self.driver.find_element_by_xpath('//div[@id="sucai_list_search_botton" and @class="sucai_list_search_botton_div"]')
    
    
    def receive_single_add_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加"按钮.')
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_move_sucai_two"]/div[@id="sucai_dialog_create_move_add"]')
    
    
    def receive_all_add_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加全部"按钮.')
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_move_sucai_two"]/div[@id="sucai_dialog_create_move_addall"]')
    
       
    def receive_single_delete_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"删除"按钮.')
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_move_sucai_two"]/div[@id="sucai_dialog_create_move_delete"]')
 
    def receive_all_delete_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"全部删除"按钮.')
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_move_sucai_two"]/div[@id="sucai_dialog_create_move_deleteall"]')
 
    def receive_specific_delete_button(self,text):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u"找到指定的需要删除的'%s'素材按钮." % text)
        return self.driver.find_element_by_xpath('//div[@id="sucai_dialog_sucaizu_selected_container"]/div[@id="sucai_dialog_sucaizu_selected"]/div/div[@class="mCustomScrollBox mCS-my-theme mCSB_vertical mCSB_inside"]/div/table/tbody/tr/td[text()="%s"]/../td[1]' % text)
 
    def click__specific_delete_button(self,text): 
        self.logger = logging.getLogger(__name__)
        self.receive_specific_delete_button(self,text).click()
        self.logger.debug(u"选中指定的需要删除的'%s'素材按钮." % text)   
        return None
    
    def receive_selected_all_add_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"所有素材选中"添加按钮.')
        return self.driver.find_element_by_xpath('//div[@id="sucai_dialog_sucaizu_selectable" and @class="styled-flow-list-container"]/table/tbody/tr/th/input')
       
    def click_selected_all_add_button(self):
        self.logger = logging.getLogger(__name__)
        self.receive_selected_all_add_button().click()
        self.logger.debug(u'点击"所有素材选中"添加按钮.')
        return None
    
    def receive_selected_all_delete_button(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"所有素材选中"删除按钮.')
        return self.driver.find_element_by_xpath('//div[@id="sucai_dialog_sucaizu_selected" and @class="styled-flow-list-container"]/table/tbody/tr/th/input')
    
    def click_selected_all_delete_button(self):
        self.logger = logging.getLogger(__name__)
        self.receive_selected_all_delete_button().click()
        self.logger.debug(u'点击"所有素材选中"删除按钮.')
        return None
 
    def receive_confirm_btn(self): 
        self.logger = logging.getLogger(__name__) 
        self.logger.debug(u'找到"确认"按钮.') 
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_opition"]/div[@id="sucai_dialog_create_botton_click" and @class="option_bottom confirm_bottom"]') 
    
    def click_confirm_btn(self): 
        self.logger = logging.getLogger(__name__)
        self.receive_confirm_btn().click()   
        self.logger.debug(u'点击新建素材组页面中"确认"按钮.') 
        return None
    
    def receive_cancel_btn(self): 
        self.logger = logging.getLogger(__name__) 
        self.logger.debug(u'找到"取消"按钮.') 
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_opition"]/div[@class="option_bottom popup_dialog_clear"]')
       
    def click_cancel_btn(self): 
        self.receive_cancel_btn().click()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击新建素材组页面中"取消"按钮.')       
        return Mgpicture(self.driver)
     
class Mgvideo(Basepage):
    def rec_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"添加素材"按钮.')
        return self.driver.find_element_by_xpath('//div[@id="sucai_add_class_btn"]/span')

    def click_create_btn(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'点击"新建广告位 "按钮.')
        self.rec_create_btn().click()
        return CreateMaterialGroupForVideo(self.driver)
    
    def rec_new_material_info_for_video(self):       
        self.logger = logging.getLogger(__name__)
        material_info=[]
        self.logger.debug(u'获取"最后一页的素材信息".')   
        trs = self.driver.find_elements_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr')
        num = 0
        for tr in trs:
            material_name = tr.find_element_by_xpath('.//td[1]').text
            self.logger.debug(u'素材名称为  %s.'  % material_name)  
            if material_name == "":
                break
            num = num + 1
        self.logger.debug(u'num为  %s".'  % num)  
        material_name =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[1]' % num ).text
        self.logger.debug(u'素材名称为  %s".'  % material_name)  
        material_info.append( material_name )
        
        material_status =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[2]' % num ).text
        material_info.append( material_status )
        
        material_author =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[3]' % num ).text
        material_info.append(  material_author ) 
        
        material_size =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[4]' % num ).text
        material_info.append( material_size )
        
        material_time =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[5]' % num ).text
        material_info.append( material_time ) 
        
        material_weigh =  self.driver.find_element_by_xpath('//div[@id="sucai_container"]/div[@id="sucai_content"]/div[@id="sucai_content_table"]/table/tbody/tr[%s]/td[6]' % num ).text
        material_info.append( material_weigh )
        
        return material_info

   
class CreateMaterialGroupForVideo(Basepage):
    def receive_material_name_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材名称"input.')
        return self.driver.find_element_by_css_selector('input#sucai_dialog_create_input_name_value')
    
    def receive_sucai_width_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的宽"input.')
        return self.driver.find_element_by_css_selector('input#sucai_dialog_create_input_size_width')
    
    def receive_sucai_height_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"尺寸的高 "input.')
        return self.driver.find_element_by_css_selector('input#sucai_dialog_create_input_size_height')    
    
    
    def receive_sucai_time_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"素材时长 "input.')
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_size"]/input[@id="sucai_dialog_create_input_time_value"]')    
    
    
    def select_weight(self,text):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u"点击'%s'" % text)
        if text in [10,30,50,70,100]:
            self.driver.find_element_by_xpath('//div[@id="sucai_dialog_create_morenguanggaowei_select"]/div[@class="select-status select-box"]/ul/li[text()="%s"]' % text).click()
        else:
            self.logger.error(u"输入权重错误！")
        return None    
       
    def receive_material_select_input(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(u'找到"选择素材"input.')
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_source"]/div[@id="sucai_dialog_create_uploadfile_source"]/input[@id="sucai_dialog_create_video_uploadfile_url"]')
      
    def receive_confirm_btn(self): 
        self.logger = logging.getLogger(__name__) 
        self.logger.debug(u'找到"确认"按钮.') 
        return self.driver.find_element_by_xpath('//div[@class="sucai_dialog_create_opition"]/div[@id="sucai_dialog_create_botton_click"]') 
    
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
        return Mgpicture(self.driver)  

 