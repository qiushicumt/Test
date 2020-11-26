#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_upload_file.py
@time:2020/11/26
"""

from selenium import webdriver
# 文件上传
def get_upload():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    input("...")
    driver.quit()

if __name__ == '__main__':
    get_upload()
