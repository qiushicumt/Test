#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_html5.py
@time:2020/11/26
"""
from selenium import webdriver

# selenium调用HTML5标签进行视频播放

def get_html5():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://localhost:8088/shopxo")

    input("...")
    driver.quit()

if __name__ == '__main__':
    get_html5()
