#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_xpath_get_attribute.py
@time:2020/11/25
"""

from selenium import webdriver

# xpath属性选择器
# 属性选择器使用[]
# 语法：//*[@class='am-container header']
# 属性名称前必须用@，属性的值则必须用'属性值'引起来
# 多个属性：//input[@id='search-input'][@name='wd']
# 多个属性必须紧挨着写，每个属性都使用[]引起来
def getAttribute():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://localhost:8088/shopxo")

    driver.find_element_by_xpath("//*[@class='am-container header']").click()       # 找到class属性为"am-container header"的元素
    driver.find_element_by_xpath("//input[@id='search-input'][@name='wd']").send_keys("手机")

    input("...")
    driver.quit()

if __name__ == '__main__':
    getAttribute()
