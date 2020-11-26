# -*- coding:utf-8 -*-
# @Time:    2020/11/20 16:32
# @Author:  mayday
# @File:    test.py

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost:8088/shopxo/")
driver.find_element_by_id("search-input").send_keys("手机")
driver.find_element_by_id("ai-topsearch").click()
input("press any key to continue...")
driver.quit()
