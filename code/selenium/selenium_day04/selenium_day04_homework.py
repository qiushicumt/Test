#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_day04_homework.py
@time:2020/11/25
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 9.打开 12306 网站  https://kyfw.12306.cn/otn/leftTicket/init
# 出发城市 填写 ‘北京’， 到达城市 填写 ‘上海’
# 发车时间 选 06:00--12:00
# 发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
# 我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息（这里可以用xpath），结果如下：
# G7641
# G1505
# G7393
# G7689
# 考察点：xpath,css,回车
def get_12306():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://kyfw.12306.cn/otn/leftTicket/init")

    # 出发地输入框输入北京
    driver.find_element_by_css_selector("#fromStationText").click()
    driver.find_element_by_css_selector("#fromStationText").send_keys("北京")
    driver.find_element_by_css_selector("#fromStationText").send_keys(Keys.DOWN)
    driver.find_element_by_css_selector("#fromStationText").send_keys(Keys.DOWN)
    driver.find_element_by_css_selector("#fromStationText").send_keys(Keys.ENTER)

    # 目的地输入框输入上海
    driver.find_element_by_css_selector("#toStationText").click()
    driver.find_element_by_css_selector("#toStationText").send_keys("上海")
    driver.find_element_by_css_selector("#toStationText").send_keys(Keys.ENTER)

    # 选择发车时间
    driver.find_element_by_css_selector("#cc_start_time").click()
    driver.find_element_by_css_selector("#cc_start_time option:nth-child(3)").click()

    # 选择发车日期
    driver.find_element_by_css_selector("#train_date").click()
    driver.find_element_by_css_selector(".cal-cm>div[style^='border']+div").click()    # 选择当前日期的下一个兄弟元素

    # 点击查询按钮
    driver.find_element_by_css_selector("#query_ticket").click()

    # 分析查询结果
    trs = driver.find_elements_by_xpath("//tr[contains(@datatran,'G')]/preceding-sibling::tr[1]")

    for tr in trs:
        if tr.find_element_by_css_selector("td:nth-child(4)").text == "有":
            print(tr.find_element_by_css_selector(".ticket-info a:nth-child(1)").text)

    input("Press any key to continue...")
    driver.quit()

# 10.登录华为官网 https://www.vmall.com/，
# 点击 "华为官网" 和  "华为应用市场" 两个链接。
# 检查 "华为官网" 页面上导航菜单与需求是否保持一致
# 检查 更多-应用市场 页面上导航菜单与需求是否保持一致
# 最后再回到主窗口， 检查鼠标停留在 "笔记本" 处的时候， 检查二级菜单与需求是否保持一致
#
# 考察点：多窗口，鼠标悬停
def get_vmall():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.vmall.com/")

    driver.find_element_by_css_selector(".s-sub li:nth-child(2)").click()   #   找到华为官网的链接，点击
    driver.maximize_window()
    ele = driver.find_element_by_css_selector(".s-sub li:nth-last-child(1) .s-dropdown")    #   找到更多精彩的元素
    ac = ActionChains(driver)
    ac.move_to_element(ele).perform()   #   鼠标悬停
    driver.find_element_by_css_selector(".dropdown-more dt:nth-child(2)").click()
    #driver.maximize_window()
    main = driver.current_window_handle     # 保存当前窗口句柄

    for one in driver.window_handles:
        driver.switch_to.window(one)
        if driver.current_url == "https://consumer.huawei.com/cn/":
            print(driver.find_element_by_css_selector(".main-nav").text)
        elif driver.current_url == "https://consumer.huawei.com/cn/":
            print(driver.find_element_by_css_selector(".center").text)

    driver.switch_to.window(main)
    ele = driver.find_element_by_css_selector("#zxnav_1")
    ac.move_to_element(ele).perform()
    print(driver.find_element_by_css_selector("#zxnav_1 .category-panels").text)

    input("Press any key to continue...")
    driver.quit()

if __name__ == '__main__':
    get_12306()
    get_vmall()