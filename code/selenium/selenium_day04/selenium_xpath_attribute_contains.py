#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_xpath_attribute_contains.py
@time:2020/11/25
"""

# 属性包含
# 通过属性值包含某个内容来定位元素
# 语法：//[contains(@属性名,'属性值')]
from selenium import webdriver

def getAttributeContains():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://localhost:8088/shopxo")

    driver.find_element_by_xpath("//input[contains(@id, 'search')]").send_keys("笔记本电脑")     # 查找id值中包含search字符串的input元素

    input("...")
    driver.quit()

if __name__ == '__main__':
    getAttributeContains()
