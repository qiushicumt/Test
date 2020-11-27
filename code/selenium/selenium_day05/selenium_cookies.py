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
from pprint import pprint

from selenium import webdriver

def get_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo")

    # 打开登录页面，进行账号登录
    driver.find_element_by_css_selector(".menu-hd a[href*='logininfo']").click()
    driver.find_element_by_css_selector("input[name='accounts']").send_keys("test01")
    driver.find_element_by_css_selector("input[name='pwd']").send_keys("123456")
    driver.find_element_by_css_selector("button[type='submit'].btn-loading-example").click()

    # 获取所有cookie
    pprint(driver.get_cookies())     # get_cookies()返回的是一个字典列表，cookie中的内容存放在一个字典中
    pprint(type(driver.get_cookies()))
    pprint(type(driver.get_cookies()[0]))
    # 获取指定的cookie
    print(driver.get_cookie("PHPSESSID"))       # 获取键的值为 “PHPSESSID” 的cookie

    # 增加cookie
    driver.add_cookie({'name':'user1', 'value':'123456'})       # 添加cookie时，按照字典的形式进行添加
    pprint(driver.get_cookies())

    # 删除cookie
    print("################################删除cookie")
    driver.delete_cookie("user1")       # 删除cookie时，传递的参数为cookie中存在的键的值
    pprint(driver.get_cookies())

    input("...")
    driver.quit()

if __name__ == '__main__':
    get_cookie()
