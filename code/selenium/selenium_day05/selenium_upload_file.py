#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_upload_file.py
@time:2020/11/26
"""

from selenium import webdriver
# 文件上传
# 思路是：将文件在电脑中的存放的路径，通过input标签的sendkeys发送到服务器，完成文件的上传

# 打开shopxo的个人中心，修改个人头像上传照片
def get_upload():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:8088/shopxo/index.php?s=/index/user/logininfo.html")

    # 登录账号
    driver.find_element_by_css_selector("input[name='accounts']").send_keys("test01")
    driver.find_element_by_css_selector("input[name='pwd']").send_keys("123456")
    driver.find_element_by_css_selector("button[type='submit'].am-btn-sm").click()

    # 修改个人资料
    driver.find_element_by_css_selector(".user-base-left .am-icon-street-view").click()


    input("...")
    driver.quit()

if __name__ == '__main__':
    get_upload()
