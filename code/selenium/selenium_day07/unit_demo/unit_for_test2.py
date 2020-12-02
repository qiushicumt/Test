#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:frankzhong
@file:unit_for_test2.py
@time:2020/12/01
"""
import unittest
import time
from selenium import webdriver

class UnitForTest2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.0.104:8088/shopxo/index.php?s=/index/user/logininfo.html")

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    def test_loginCase1(self):
        self.driver.find_element_by_name("accounts").send_keys("test01")
        self.driver.find_element_by_name("pwd").send_keys("123456")
        self.driver.find_element_by_css_selector(".form-validation button").click()

    def test_loginCase2(self):
        self.driver.find_element_by_name("accounts").send_keys("test01")
        self.driver.find_element_by_name("pwd").send_keys("666666")
        self.driver.find_element_by_css_selector(".form-validation button").click()

if __name__ == '__main__':
    unittest.main(verbosity=2)
