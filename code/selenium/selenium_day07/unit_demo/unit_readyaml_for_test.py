#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:frankzhong
@file:unit_readyaml_for_test.py
@time:2020/12/03
"""
from selenium import webdriver
import unittest
import time
from ddt import ddt, data, file_data

@ddt
class UnitReadYamlForTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.0.104:8088/shopxo/index.php?s=/index/user/logininfo.html")

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    # 通过file_data装饰器可以直接读取yaml文件中的内容
    @file_data("test_data.yaml")
    def test_loginTest(self, **user):       # **user表示按照字典的形式将数据传递给user
        self.driver.find_element_by_name("accounts").send_keys(user.get("name"))
        self.driver.find_element_by_name("pwd").send_keys(user.get("password"))
        self.driver.find_element_by_css_selector(".form-validation button").click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
