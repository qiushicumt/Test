#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:test.py
@time:2020/11/25
"""
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

def get_51job():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get("https://www.51job.com/")
    # 进入高级搜索
    driver.find_element_by_css_selector(".ush.top_wrap>a").click()

    # 查找输入框，输入搜索文字
    driver.find_element_by_css_selector("#kwdselectid").send_keys("软件测试")

    # 点击地区按钮，选择上海地区
    driver.find_element_by_css_selector("#work_position_input").click()
    spans = driver.find_elements_by_css_selector("#work_position_click_multiple_selected>span")     #   获取多选的工作地区的div的第一个span元素，形成列表
    for one in spans:
        one.click()     #   清除所有已经被选择的地区
    driver.implicitly_wait(1)
    driver.find_element_by_css_selector("#work_position_click_center_right_list_category_000000_020000").click()     #   选中上海地区
    driver.find_element_by_css_selector("#work_position_click_bottom_save").click()

    # 点击空白区域使搜索框的下拉菜单关闭掉
    driver.find_element_by_css_selector(".tit").click()

    # 点职能列表，选择测试->软件测试工程师
    # 点击职能按钮
    driver.find_element_by_css_selector("#funtype_click").click()
    driver.find_element_by_css_selector("#funtype_click_center_right_list_category_0100_2700").click()  # 点击测试按钮
    driver.find_element_by_css_selector("#funtype_click_center_right_list_sub_category_each_0100_2707").click()  # 点击软件测试工程师按钮
    driver.find_element_by_css_selector("#funtype_click_bottom_save").click()  # 点击确定按钮，保存选择

    # 选择工作年限
    driver.find_element_by_css_selector("#workyear_list>span").click()
    driver.find_element_by_css_selector("#workyear_list div.ul span[title='1-3年']").click()

    # 点击搜索按钮进行职位搜索
    driver.find_element_by_css_selector(".p_sou span").click()

    # 分析搜索结果
    divs = driver.find_elements_by_css_selector(".j_joblist>div")   #   获取所有搜索结果的div生成列表
    for div in divs:        #   对div列表进行遍历
        result_list = []
        eles = div.find_elements_by_css_selector(".t span, .info span, .er a, .er p")
        for ele in eles:
            result_list.append(ele.text)
        print('|'.join(result_list))

    input('...')
    driver.quit()

def get_163Music():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://music.163.com/")

    # 打开排行榜页面
    driver.find_element_by_css_selector("#g_nav2 li:nth-child(2) a").click()

    # 榜单列表是另外的一个frame，切换进入另外一个frame
    driver.switch_to.frame("g_iframe")

    # 获取歌曲榜单列表
    song_list = driver.find_elements_by_css_selector(".m-table-rank tbody tr")      #   将一百首歌曲生成一个列表

    #分析数据
    # 遍历歌曲列表
    for one in song_list:
        result_list = []
        eles = one.find_elements_by_css_selector(".hd>span, .ttc b, .u-dur , .text")    #   获取被打印的内容的元素，生成一个列表
        for ele in eles:
            if ele.get_attribute("title"):      #   元素具有title属性，则返回title属性的字符串，不具有title属性，则返回空行
                result_list.append(ele.get_attribute("title"))
            else:
                result_list.append(ele.text)    #   不具有title属性的元素获取其text值
        print('|'.join(result_list))

    input("Press any key to continue...")
    driver.quit()

if __name__ == '__main__':
#    get_51job()
    get_163Music()