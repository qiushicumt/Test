#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Administrator
@file: unit_readdata_for_test
@time: 2020/12/3
"""
import unittest
import time
from selenium import webdriver
from ddt import ddt, data, unpack

def read_data():
    """
    读取文件中内容
    :return: 返回读取的内容
    """
    read_file = open("read_data.txt", "r", encoding="utf8")
    data_list = []
    for one in read_file.readlines():
        data_list.append(one.strip("\n").split(","))
    return data_list

# 给类添加ddt装饰器，表示类中会使用ddt处理数据
@ddt
class UnitReadDataForTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """
        类前置条件
        :return: None
        """
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        """
        类后置条件
        :return: None
        """
        pass

    def setUp(self) -> None:
        """
        测试用例函数的前置条件
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:8088/shopxo/public/index.php?s=/index/user/logininfo.html")

    def tearDown(self) -> None:
        """
        测试用例函数的后置条件
        :return:
        """
        time.sleep(3)       # 关闭窗口前暂停3秒
        self.driver.quit()  # 关闭窗口

    @data(*read_data())
    @unpack
    def test_Login(self, username, passwd):
        self.driver.find_element_by_name("accounts").send_keys(username)
        self.driver.find_element_by_name("pwd").send_keys(passwd)
        self.driver.find_element_by_css_selector(".form-validation button").click()

if __name__ == "__main__":
    unittest.main(verbosity=2)