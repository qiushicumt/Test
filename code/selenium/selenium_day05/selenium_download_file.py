#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_download_file.py
@time:2020/11/26
"""
# 文件下载
# selenium通过ChromeOptions配置下载路径，禁止弹窗
# 启动Chrome定位元素下载
import os

from selenium import webdriver

def get_download():
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    # 配置ChromeOptions
    options = webdriver.ChromeOptions()         # ChromeOptions是配置Chrome启动时的配置信息的类
    prefs = {
        'profile.default_content_setting.popups': 0,        # 设置此项为0，表示禁止弹出下载的弹窗
        'download.default_directory': os.getcwd(),          # 设置默认的下载路径
    }
    options.add_experimental_option('prefs', prefs)         # 将Chrome配置信息加载到options中

    driver = webdriver.Chrome(options=options)              # 用配置好的Chrome生成一个chrome窗口

    # 打开网页并进行下载
    driver.get("https://weixin.qq.com/cgi-bin/readtemplate?uin=&stype=&promote=&fr=&lang=zh_CN&ADTAG=&check=false&t=weixin_download_method&sys=android&loc=weixin,android,web,0")
    driver.find_element_by_css_selector("#downloadBtn32").click()

    input("...")
    driver.quit()

if __name__ == '__main__':
    get_download()
