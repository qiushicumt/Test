#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_xpath_buchong.py
@time:2020/11/25
"""
from selenium import webdriver
# xpath补充选择
def buchong():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://localhost:8088/shopxo")

    input("...")
    driver.quit()

if __name__ == '__main__':
    buchong()
