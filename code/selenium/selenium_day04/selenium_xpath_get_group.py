#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_xpath_get_group.py
@time:2020/11/25
"""
from selenium import webdriver
# xpath组选择器
# xpath的组选择使用 | 符号，将两个选择的元素连在一起
# 返回的是多个元素，组成列表
# 语法： //*[]|//*[]
def getGroup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://localhost:8088/shopxo")

    eles = driver.find_elements_by_xpath("//*[@id='search-input']|//*[@id='ai-topsearch']")
    for ele in eles:
        print(ele.get_attribute("outerHTML"))

    input("...")
    driver.quit()

if __name__ == '__main__':
    getGroup()
