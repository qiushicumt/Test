#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:frankzhong
@file:unit_readdata_for_test.py
@time:2020/12/02
"""
from selenium import webdriver
import unittest
import time
from ddt import data,unpack,ddt

def read_data():
    """
    读取外部数据
    :return: 返回一个列表
    """
    read_file = open("data.txt", "r", encoding="utf8")
    li = []
    for one in read_file.readlines():
        li.append(one.strip("\n").split(","))
    read_file.close()
    return li


@ddt
class UnitReadDateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.0.105:8088/shopxo/index.php?s=/index/user/logininfo.html")

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    @data(*read_data())
    @unpack
    def test_readDataForTest(self, username, passwd):
        """
        测试通过读取外部数据登录
        :param username: 用户名
        :param passwd: 密码
        :return: None
        """
        self.driver.find_element_by_name("accounts").send_keys(username)
        self.driver.find_element_by_name("pwd").send_keys(passwd)
        self.driver.find_element_by_css_selector(".form-validation button").click()

if __name__ == '__main__':
    unittest.main(verbosity=2)
