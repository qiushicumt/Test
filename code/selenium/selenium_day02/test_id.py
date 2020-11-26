#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:test_id.py
@time:2020/11/23
"""

from selenium import webdriver

def baidu():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("汇智动力")
    driver.find_element_by_id("su").click()
    # driver.find_element_by_id(3)
    list1 = driver.find_elements_by_tag_name("a")
    print(len(list1))
    input("press anykey to continue")
    driver.quit()

if __name__ == '__main__':
    baidu()
