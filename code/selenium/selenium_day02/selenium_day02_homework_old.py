#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_day02_homework.py
@time:2020/11/23
"""

# 4.获取江苏省最低温度城市
# http://www.weather.com.cn/html/province/jiangsu.shtml
# 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如
# 温度最低为12℃, 城市有连云港 盐城。
# 考察点：id,tag name,finds_element_by_xx

from selenium import webdriver

def find_weather():
    driver = webdriver.Chrome()     # 获取WebDriver对象
    driver.implicitly_wait(10)
    driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")      # 打开浏览器页面
    result = driver.find_element_by_id("forecastID").text
    list1 = result.split()
    list_c = []
    list_t = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list_c.append(list1[i])
        else:
            list_t.append(list1[i])
    print(list_c)       #   城市列表
    print(list_t)       #   温度列表
    tmp_str = "/".join(list_t)      #   温度列表合成字符串
    tmp_str += "/"
    list_t = tmp_str.split("℃/")    #   字符串切割去掉"℃/"
    list_t.pop()                    #   去掉最后的空元素
    list_t_low = []
    dict1={}
    for i in range(len(list_t)):    #   遍历将最低温度放入list_t_low列表中
        if i%2 == 0:
            list_t_low.append(list_t[i])
    for one in list_t_low[:]:
        if one not in dict1:
            dict1[one] = [list_c[list_t_low.index(one)]]
        else:
            dict1[one].append(list_c[list_t_low.index(one)])

    print(dict1)

    # low_temp = min(list_t_low)
    # list_c_tmp = []
    # dict1 = dict.fromkeys(list_c)
    # print(dict1)
    # while len(low_temp)>1:
    #     for one in low_temp[:]:
    #         if one == min(low_temp):
    #             l_index = low_temp.index(one)
    #             list_c_tmp.append(list_c[l_index])
    #             # low_temp.removeprefix(one)

    input("press anykey to continue...")
    driver.quit()

if __name__ == '__main__':
    find_weather()
