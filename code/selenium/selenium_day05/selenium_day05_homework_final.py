#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_day05_homework_final.py
@time:2020/11/27
"""
from selenium import webdriver
import time

# 12.修改账号的个人资料的头像为兔斯基头像，昵称为兔斯基，性别为男，2006-1-1
# 考察点：单选框 上传文件
def get_changeInfo():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo")
    # 登录账号
    driver.find_element_by_css_selector(".top-nav-left .menu-hd a:nth-child(3)").click()  # 点击登录
    driver.find_element_by_css_selector("[name='accounts']").send_keys("test01")  # 输入账号test01
    driver.find_element_by_tag_name("[name='pwd']").send_keys("123456")  # 输入账号的密码
    driver.find_element_by_tag_name("[name='pwd']").submit()
    time.sleep(3)

    # 进入个人中心
    driver.find_element_by_css_selector(".top-nav-right>div:nth-of-type(1) span").click()  # 点击个人头像打开个人中心
    driver.find_element_by_css_selector(".am-icon-edit").click()  # 点击修改资料

    # 修改头像
    driver.find_element_by_css_selector(".dl-content dd:nth-of-type(1) .span-edit").click()
    driver.find_element_by_css_selector("input[name='file']").send_keys(r"E:\Working\workspace\selenium\Selenium\selenium_day05\2.jpg")
    driver.find_element_by_css_selector("button[type='submit'].head-submit").click()
    time.sleep(3)

    # 编辑个人资料
    driver.find_element_by_css_selector("legend .am-fr").click()
    # 修改昵称
    driver.find_element_by_css_selector("input[name='nickname']").clear()
    driver.find_element_by_css_selector("input[name='nickname']").send_keys("兔斯基")
    # 修改性别
    driver.find_element_by_css_selector(".am-form-group label:nth-of-type(3) .am-icon-checked").click()
    # 修改生日
    driver.find_element_by_css_selector("input[name='birthday']").clear()
    driver.find_element_by_css_selector("input[name='birthday']").send_keys("2006-01-01")   # 通过直接输入的方式输入生日

    # 保存修改信息
    driver.find_element_by_css_selector(".am-form-group-refreshing button[type='submit']").click()

    input("...")
    driver.quit()

# 13.使用cookies技巧绕过shopxo登录验证码
# 考察点：cookies
def get_cookies():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo")

    # 进入登录页面，进行第一次登录
    driver.find_element_by_css_selector(".top-nav-left a:nth-of-type(1)").click()
    driver.find_element_by_css_selector("[name='accounts']").send_keys("test01")  # 输入账号test01
    driver.find_element_by_tag_name("[name='pwd']").send_keys("123456")  # 输入账号的密码
    input("请手动输入验证码...")
    driver.find_element_by_tag_name("[name='pwd']").submit()

    # 获取cookie
    list1 = driver.get_cookies()     # get_cookie返回cookie的字典
    driver.quit()       # 关闭会话窗口

    # 重新打开
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo")
    driver.find_element_by_css_selector(".top-nav-left a:nth-of-type(1)").click()   # 重新进入登录页面
    driver.delete_all_cookies()     # 删除cookie

    # 向当前cookie中添加信息
    for one in list1:
        driver.add_cookie({'name':one['name'], 'value':one['value']})       # 添加的cookie添加的是字典

    driver.refresh()

    input(...)
    driver.quit()

if __name__ == '__main__':
    # get_changeInfo()
    get_cookies()