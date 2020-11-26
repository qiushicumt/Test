#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:selenium_selector.py
@time:2020/11/24
"""
from selenium import webdriver

# 1、简单选择器：简单选择器包含 . # 标签
def simple_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()

# 2、并列选择器：多个选择条件连着写
def binglie_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()

# 3、后代选择器：通过空格连接父亲和孩子
def houdai_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()

# 4、子选择器：选择当前元素的儿子选择器
def son_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()

# 5、通用选择器：通配符，适配所有的元素
def tongyong_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()

# 6、群组选择器：
def group_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()

# 7、兄弟选择器：一般用于选择弟弟元素
def brother_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()

# 8、属性选择器：
def shuxing_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()


# 9、
# .menu-hd>a:nth-last-child(1)
#
# .menu-hd>*:not(a)
# nth-child  父亲第几个孩子，与标签名无关
# nth-last-child 父亲倒数第几个孩子，也与标签名无关
# nth-of-type 标签的第几个
# nth-last-type 标签的倒数第几个

def nth_selector():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    input("Press any key to continue...")
    driver.quit()


if __name__ == '__main__':
    pass
