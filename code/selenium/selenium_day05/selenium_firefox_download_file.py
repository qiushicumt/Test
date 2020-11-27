#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_firefox_download_file.py
@time:2020/11/27
"""
import os

from selenium import webdriver
# Firefox浏览器下载文件会先弹窗询问下载文件及路径

def get_firefox_download():
    # 配置Firefox
    fp = webdriver.FirefoxProfile()     # 进行Firefox的配置
    fp.set_preference("browser.download.folderlist", 2)         # 0:设置文件下载到浏览器默认路径  2:设置文件下载到指定目录
    fp.set_preference("browser.download.dir", os.getcwd())      # 设置文件下载到项目文件所在的目录
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")      # 设置下载文件的后缀格式

    # 生成一个Firefox窗口
    driver = webdriver.Firefox(firefox_profile=fp, executable_path=r"D:\webdriver\geckodriver.exe")

    # 打开网页下载文件
    driver.get("http://npm.taobao.org/mirrors/chromedriver/")
    driver.find_element_by_css_selector("a[href$='87.0.4280.20/']").click()     # 下载chrome webdriver
    driver.find_element_by_css_selector("a[href$='win32.zip']").click()

if __name__ == '__main__':
    get_firefox_download()
