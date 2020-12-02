#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:frankzhong
@file:unit_for_test.py
@time:2020/12/01
"""
# 导入unittest包
import unittest

# 定义一个UnitForTest的类
class UnitForTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    # 每一条测试用例的前置条件
    def setUp(self) -> None:
        print("setUp")

    # 每一条测试用例的后置条件
    def tearDown(self) -> None:
        print("tearDown")

    # 测试用例 test_case2
    def test_case2(self):
        print("this is TestCase2")

    # 测试用例 test_case1
    def test_case1(self):
        print("this is TestCase1")


if __name__ == '__main__':
    unittest.main(verbosity=2)
