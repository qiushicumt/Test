#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:frankzhong
@file:unit_ddt_for_test.py
@time:2020/12/01
"""
import unittest
import time

from selenium import webdriver
from ddt import ddt, data, unpack

# 使用装饰器ddt修饰类，表明类中要使用ddt进行数据分离
@ddt
class UnitDdtForTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        """ 前置条件 """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.0.104:8088/shopxo/index.php?s=/index/user/logininfo.html")

    def tearDown(self) -> None:
        """ 后置条件 """
        time.sleep(2)
        self.driver.quit()

    # @data()装饰器用于向函数中传入参数，传入多个参数时使用list传参
    # @unpack用于对传入的参数进行解包
    @data(['test01', '123456'], ['test01', '666666'])
    @unpack
    def test_login(self, username, passwd):
        self.driver.find_element_by_name("accounts").send_keys(username)
        self.driver.find_element_by_name("pwd").send_keys(passwd)
        self.driver.find_element_by_css_selector(".form-validation button").click()

if __name__ == '__main__':
    unittest.main(verbosity=2)
