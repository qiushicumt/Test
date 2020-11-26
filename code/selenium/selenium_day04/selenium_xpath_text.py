#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_xpath_text.py
@time:2020/11/25
"""

from selenium import webdriver

# xpath获取元素文本
# 通过xpath可以获取元素的文本，即使元素不是超链接
# //*[text()='个人中心']
# find_element_by_xpath()   找到匹配的第一个元素
# find_elements_by_xpath()  找到匹配的所有元素
def getText():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://localhost:8088/shopxo")

    driver.find_element_by_xpath("//*[text()='登录']").click()    # 找到匹配“登录”的第一个元素并点击

    input("...")
    driver.quit()

if __name__ == '__main__':
    getText()
