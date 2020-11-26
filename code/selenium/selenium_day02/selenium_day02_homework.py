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
    tmp_str = "/".join(list_t)      #   温度列表合成字符串
    tmp_str += "/"
    list_t = tmp_str.split("℃/")    #   字符串切割去掉"℃/"
    list_t.pop()                    #   去掉最后的空元素
    list_t_low = []
    dict1={}
    for i in range(len(list_t)):    #   遍历将最低温度放入list_t_low列表中
        if i%2 == 0:
            list_t_low.append(list_t[i])
    for i in range(len(list_t_low)):
        if list_t_low[i] not in dict1:
            dict1[list_t_low[i]] = [list_c[i]]
        else:
            dict1[list_t_low[i]].append(list_c[i])

    list2 = []
    for i in range(len(list_t_low)):
        list2.append(int(list_t_low[i]))

    print(f"温度最低为{min(list2)}℃，城市有{''.join(dict1[str(min(list2))])}")

    input("press anykey to continue...")
    driver.quit()

# 通过对获得的整体的字符串进行切割，切割出想要的城市和温度
def find_weather1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")
    str = driver.find_element_by_id("forecastID").text
    list1 = str.split("℃\n")        #       将获得的字符串以"℃\n"进行切割
    temp_list = []
    dict1 = {}
    for one in list1:
        city = one.split("\n")[0]     #       以"\n"对列表中每一个字符串进行切割，得到的列表取列表中第一个元素得到城市名
        temp = one.split("/")[1]      #       以"/"对列表中每一个字符串进行切割，得到的列表取列表中第二个元素得到温度
        temp = temp.replace("℃", "")        #   将包含℃的字符串的℃替换为空
        temp = int(temp)
        temp_list.append(temp)
        if temp not in dict1:
            dict1[temp] = [city]
        else:
            dict1[temp].append(city)
    print(f"温度最高为{min(temp_list)}℃，城市有{''.join(dict1[min(temp_list)])}")

    input("press anykey to continue...")
    driver.quit()

# 通过html标签特征，直接找到对应的城市和温度
def find_weather2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")
    dl_list = driver.find_element_by_id("forecastID").find_elements_by_tag_name("dl")
    temp_list = []
    dict1 = {}
    for one in dl_list:
        city = one.find_element_by_tag_name("a").text       # 通过标签<a>的text属性，得到城市名
        temp = one.find_element_by_tag_name("b").text       # 通过标签<b>的text属性，得到温度
        temp = temp.replace("℃", "")        # 将得到的温度字符串末尾的℃替换为空格
        temp = int(temp)                    # 对得到的温度进行整型变换
        # 构造温度列表和温度/城市的字典
        temp_list.append(temp)
        if temp not in dict1:
            dict1[temp] = [city]        # 如果温度对应的键在字典中没有出现，则新建一个键值对，键对应的值为城市列表
        else:
            dict1[temp].append(city)        # 当键已经存在时，dict1[temp]则为一个城市列表，通过append方法，可以新增城市名到列表中
    print(f"温度最高为{min(temp_list)}℃，城市有{''.join(dict1[min(temp_list)])}")
    input("press any key to continue...")
    driver.quit()

if __name__ == '__main__':
#     find_weather()
    find_weather1()
    # find_weather2()
