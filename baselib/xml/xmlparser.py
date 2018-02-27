#!/usr/bin/env python
# -*- coding: utf-8 -*-   
from lxml import etree
import re
import logging
from baselib.logging.pylogging import setup_logging
setup_logging()
logger = logging.getLogger(__name__)

"""This function modify xml element attribute value.
    The arguments are:
            - filename         : xml file.
            - xpath            : the xml file element xpath expression.
            - attr             : the xml file element attribute name.
            - value            : the xml file element attribute name.
    
    Example:

         >>> modify_attr("c:\\data.xml", "/data/country/neighbor[@name='Austria1']","age","40")  
"""
def modify_attr(filename,xpath,attr,value):
    parser = etree.XMLParser( remove_blank_text=True, resolve_entities=True, strip_cdata=True)
    tree = etree.parse(filename,parser)
    elements = tree.xpath(xpath)
    if len(elements) == 0:
        logger.debug("can not find the elememt %s." % xpath)
        return False
    else:
        for element in elements: 
            element.attrib[attr] = value
        tree.write(filename,encoding="utf-8",xml_declaration="true",pretty_print="True"  ) 
        return True
        
"""This function get xml element attribute value,if the attribute is not exist,return None.
    The arguments are:
            - filename         : xml file.
            - xpath            : the xml file element xpath expression.
            - attr             : the xml file element attribute name.
    
    Example:
         >>> modify_attr("c:\\data.xml", "/data/country/neighbor[@name='Austria1']","age")  
"""    
def get_attr_value(filename,xpath,attr): 
    parser = etree.XMLParser( remove_blank_text=True, resolve_entities=True, strip_cdata=True)
    tree = etree.parse(filename,parser)
    attrs = tree.xpath( xpath + "/@" + attr)
    if len(attrs) == 0:
        logger.debug("can not find the attribute %s" % attr)
        return False
    elif len(attrs) >= 0:
        logger.debug("find many attribute %s,the xpath expression is wrong" % attr)
        return False
    else:
        return attrs[0]
            
"""This function remove xml element attribute,if the attribute is not exist,return False.
    The arguments are:
            - filename         : xml file.
            - xpath            : the xml file element xpath expression.
            - attr             : the xml file element attribute name.
    
    Example:
         >>> remove_attr("c:\\data.xml", "/country/neighbor[@name='Austria1']","age")  
"""    
def remove_attr(filename,xpath,attr):  
    parser = etree.XMLParser( remove_blank_text=True, resolve_entities=True, strip_cdata=True)
    tree = etree.parse(filename,parser)
    elements = tree.xpath( xpath)
    if len(elements) == 0:
        logger.debug("can not find the attribute %s" % attr)
        return False
    elif len(elements) >= 0:
        logger.debug("find many attribute %s,the xpath expression is wrong" % attr)
        return False
    else:
        if attr in elements[0].attrib:
            del elements[0].attrib[attr] 
            tree.write(filename,encoding="utf-8",xml_declaration="true" ,pretty_print="True") 
            return True
        else:
            return False

"""This function get xml element text,if the element is not exist,return None.
    The arguments are:
            - filename         : xml file.
            - xpath            : the xml file element xpath expression.
    
    Example:
         >>> get_text("c:\\data.xml", "/country/neighbor[@name='Austria1']")  
"""    
def get_text(filename,xpath): 
    parser = etree.XMLParser( remove_blank_text=True, resolve_entities=True, strip_cdata=True)
    tree = etree.parse(filename,parser)    
    text = tree.xpath(xpath + "/text()")
    return text

"""This function set xml element text,if the element is not exist,return False.
    The arguments are:
            - filename         : xml file.
            - xpath            : the xml file element xpath expression.
            - text             : the xml file element text.
    Example:
         >>> set_text("c:\\data.xml", "/country/neighbor[@name='Austria1']","large")  
"""    
def set_text(filename,xpath,text):  
    parser = etree.XMLParser( remove_blank_text=True, resolve_entities=True, strip_cdata=True)
    tree = etree.parse(filename,parser) 
    subelements = tree.xpath(xpath)
    if len(subelements) > 0:
        for subelement in subelements:
            subelement.text = text 
        tree.write(filename,encoding="utf-8",xml_declaration="true",pretty_print="True"  ) 
        return True
    else:
        logger.debug("can not find the element %s" % xpath)
        return False

"""This function remove xml element,if the element is not exist,return False.
    does not support remove root element.
    The arguments are:
            - filename         : xml file.
            - xpath            : the xml file element xpath expression.
    Example:
         >>> remove_element("c:\\data.xml", "/country/neighbor[@name='Austria1']")  
"""    
def remove_element(filename,xpath):  
    parser = etree.XMLParser( remove_blank_text=True, resolve_entities=True, strip_cdata=True)
    tree = etree.parse(filename,parser) 
    elements = tree.xpath(xpath)
    if len(elements) > 0:
        for element in elements:
            element.getparent().remove(element)
        tree.write(filename,encoding="utf-8",xml_declaration="true",pretty_print="True"  ) 
        return True
    else:    
        logger.debug("can not find the element %s" % xpath)
        return False
    
'''This function insert xml element.
    does not support insert root element.
    does not support insert multiple.
    The arguments are:
            - filename         : xml file.
            - xpath            : the xml file element xpath expression.
            - position         : the sequence under the parent element
            - text             : the insert element under the xpath node.
    Example:
         >>>cddata = """\
         >>>        <age name="Switzerland" direction="W">
         >>>            <hello name="xy">
         >>>                <rank>68</rank>
         >>>                <year>2011</year>
         >>>            </hello> 
         >>>        </age> 
         >>>"""
         >>> insert_element("c:\\data.xml", "/country/neighbor[@name='Austria1']" ,0 , cddata)  
'''    
def insert_element(filename,xpath,text,position = 0):  
    parser = etree.XMLParser( remove_blank_text=True, resolve_entities=True, strip_cdata=True)
    tree = etree.parse(filename,parser) 
    elements = tree.xpath(xpath)
    if len(elements) > 0:
        for element in elements:
            element.getparent().remove(element)
            element.insert(position , text)  
        tree.write(filename,encoding="utf-8",xml_declaration="true",pretty_print="True"  ) 
        return True
    else:    
        logger.debug("can not find the element %s,can not insert" % xpath)
        return False
    


"""This function change string to  xml file.
    The arguments are:
            - filename         : xml file.
            - str           : the xml sting content.
    Example:
         >>>str = \"\"\"\   <?xml version='1.0' encoding='UTF-8'?>
         >>>                <age name="Switzerland" direction="W"> 
         >>>                   <hello name="xy">   
         >>>                      <rank>68</rank>
         >>>                      <year>2011</year>
         >>>                   </hello> 
         >>>               </age>
         >>>\"\"\"
         >>>
         >>>filename = "c:\\data.xml"
         >>> str_to_xml(filename, str)  
"""  
def str_to_xml(filename,str):
    filehd = open(filename, "w+")
    filehd.write(str)
    filehd.close()