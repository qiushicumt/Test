#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:unittest_testcase.py
@time:2020/11/30
"""
import unittest
# 测试用例
class TestCalc(unittest.TestCase):      # 继承TestCase类
    # 被执行的测试用例的方法，需要以test开头去命名
    def test_004(self):
        print("测试除法")
    def test_002(self):
        print("测试减法")
    def test_003(self):
        print("测试乘法")
    def test_001(self):
        print("测试加法")
    def jde(self):
        print("a+b+c")

if __name__ == '__main__':
    # unittest的main方法，可以直接实例化一个测试类，执行测试用例
    unittest.main(verbosity=2)      # verbosity=2，表示日志等级为2

