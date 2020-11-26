#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_xpath_tongpeifu.py
@time:2020/11/25
"""
from selenium import webdriver
# xpath的通配符
def getTongPei():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://localhost:8088/shopxo")

    input("...")
    driver.quit()

if __name__ == '__main__':
    getTongPei()
