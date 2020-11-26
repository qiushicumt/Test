#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_switch_window.py
@time:2020/11/25
"""
from selenium import webdriver

def get_switch_window():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://localhost:8088/shopxo")

    driver.find_element_by_css_selector(".am-footer-miscs a[href='http://shopxo.net']").click()     # 定位页面底部的超链接，打开http://shopxo.net网站

    main = driver.current_window_handle     # 保存当前窗口的句柄
    print(driver.window_handles)  # 打印窗口的句柄
    # 切换窗口句柄
    for one in driver.window_handles:
        driver.switch_to.window(one)    # 切换到窗口
        if driver.current_url == "https://shopxo.net":      # 如果窗口的url地址为https://shopxo.net，则跳出循环，停止切换
            break

    print(driver.find_element_by_css_selector(".nav").text)

    driver.switch_to.window(main)

    driver.find_element_by_css_selector("#search-input").send_keys("手机")

    input("...")
    driver.quit()

if __name__ == '__main__':
    get_switch_window()
