#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_day05_homework.py
@time:2020/11/26
"""
from selenium import webdriver
import time
# 12.修改账号的个人资料的头像为兔斯基头像，昵称为兔斯基，性别为男，2006-1-1
# 考察点：单选框 上传文件

def get_changeInfo():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo")
    driver.find_element_by_css_selector(".top-nav-left .menu-hd a:nth-child(3)").click()        # 点击登录
    driver.find_element_by_css_selector("[name='accounts']").send_keys("test01")     # 输入账号test01
    driver.find_element_by_tag_name("[name='pwd']").send_keys("123456")             # 输入账号的密码
    driver.find_element_by_tag_name("[name='pwd']").submit()

    time.sleep(3)

    #打开个人中心
    driver.find_element_by_css_selector(".top-nav-right>div:nth-of-type(1) span").click()      # 点击个人头像打开个人中心
    driver.find_element_by_css_selector(".am-icon-edit").click()        # 点击修改资料

    #修改头像
    driver.find_element_by_css_selector(".dl-content>dd:nth-of-type(1) a").click()
    driver.find_element_by_css_selector(".am-form-group input").send_keys(r"E:\Working\workspace\selenium\Selenium\selenium_day05\1.jpg")    # 发送字符串到input中
    driver.find_element_by_css_selector(".am-form>button").click()

    time.sleep(3)
    # 修改昵称
    driver.find_element_by_css_selector("legend .am-fr").click()
    driver.find_element_by_css_selector(".user-content-body input[name='nickname']").clear()
    driver.find_element_by_css_selector(".user-content-body input[name='nickname']").send_keys("兔斯基")

    time.sleep(1)
    # 修改性别
    driver.find_element_by_css_selector(".user-content-body>form>div:nth-child(3)>div>label:nth-child(3)>span>i:nth-child(2)").click()

    # 修改生日
    driver.find_element_by_css_selector(".user-content-body>form>div:nth-child(4)").click()
    driver.switch_to.frame(1)
    driver.find_element_by_css_selector(".YMenu+input").send_keys("2006")
    driver.find_element_by_css_selector(".MMenu+input").send_keys("1")
    driver.find_element_by_css_selector(".WdateDiv>div:nth-child(3) tr:nth-of-type(2)>td[onclick='day_Click(2006,1,1);']").click()

    # 保存
    driver.find_element_by_css_selector(".user-content-body button[type='submit']").click()

    input("Press any key to continue...")
    driver.quit()

# 13.使用cookies技巧绕过shopxo登录验证码
# 考察点：cookies
def get_cookies():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo")
    driver.find_element_by_css_selector(".top-nav-left .menu-hd a:nth-child(3)")

    input("Press any key to continue...")
    driver.quit()

if __name__ == '__main__':
    get_changeInfo()
