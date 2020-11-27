#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:test.py
@time:2020/11/27
"""
from selenium import webdriver
# 登录页面的button按钮测试
def test_button():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo/index.php?s=/index/user/logininfo.html")

    driver.find_element_by_css_selector("input[name='accounts']").send_keys("test01")
    driver.find_element_by_css_selector("input[name='pwd']").send_keys("123456")
    driver.find_element_by_css_selector("button[type='submit'].btn-loading-example").click()

    input("...")
    driver.quit()

if __name__ == '__main__':
    test_button()
