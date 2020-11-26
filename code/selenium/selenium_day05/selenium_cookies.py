#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_cookies.py
@time:2020/11/26
"""
# selenium利用cookies中的内容绕过登录的验证
# 利用了用户不退出，直接关闭浏览器时，服务器端会保存用户登录的cookie信息
# 此时，通过selenium读取cookie内容进行登录，使得服务器不会验证登录

from selenium import webdriver

def get_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo")

    input("...")
    driver.quit()

if __name__ == '__main__':
    get_cookie()
