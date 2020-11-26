#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_day02_work.py
@time:2020/11/23
"""


# 1.百度首页搜索汇智动力，并检查第一条搜索结果（非广告）是否是汇智动力
# 考察点：id,sleep
#
# 2.后台关闭登录验证码，完成test01账号的登录
# 考察点: name,link text,class,tag name,sleep
#
# 3.后台关闭注册验证码，完成test02账号的注册
# 考察点：link test,class,tag name,find_elements_by_xx/submit

from selenium import webdriver
import time

def baidu_search():
    driver = webdriver.Chrome()                 # 调用驱动，生成一个webdriver对象
    driver.get("https://www.baidu.com")         # 打开浏览器，访问百度页面
    driver.find_element_by_id("kw").send_keys("汇智动力")       # 找到id为“kd”的元素，即搜索框
    driver.find_element_by_id("su").click()                     # 找到id为“su”的元素，即搜索按钮
    time.sleep(1)       # 强制延时等待1s时间，等待搜索结果的返回
    result = driver.find_element_by_id("content_left").find_element_by_id(1)        # 通过父辈元素的id“content_left”，精确定位子元素的id为1的元素
    if "www.hzdledu.com" in result.text:        # 元素属性text，表示元素所有的文本内容，在文本内容中查找“www.hzdledu.com”的内容
        print("pass")
    else:
        print("fail")
    input("press anykey to continue...")
    driver.quit()

def login_test():
    driver = webdriver.Chrome()     # 生成driver对象
    driver.get("http://localhost:8088/shopxo")      # 打开浏览器，访问前端页面
    driver.find_element_by_link_text("登录").click()      # 打开登录页面
    driver.find_element_by_name("accounts").send_keys("user1")      # 找到用户名输入框输入user1
    driver.find_element_by_name("pwd").send_keys("123456")          # 找到密码输入框输入登录密码
    driver.find_element_by_class_name("am-form").find_element_by_class_name("am-btn").click()       # 通过找到按钮的父元素form，定位到表单中的登录按钮
    # driver.find_element_by_name("pwd").submit()
    input("press anykey to continue...")
    driver.quit()

def register_test():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8088/shopxo")
    driver.find_element_by_link_text("注册").click()
    list1 = driver.find_element_by_class_name("am-form").find_elements_by_tag_name("input")   #   获取form表单中
    # driver.find_element_by_name("accounts").send_keys("test02")
    list1[0].send_keys("test02")
    list1[1].send_keys("123456")
    # driver.find_element_by_name("is_agree_agreement").click()
    driver.find_element_by_class_name("am-icon-checked").click()
    list1[1].submit()
    input("press anykey to continue...")
    driver.quit()

if __name__ == '__main__':
    baidu_search()
    # login_test()
    # register_test()
