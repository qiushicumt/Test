#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:unittest_testsuite.py
@time:2020/11/30
"""
import unittest
# 测试套件
# 通过unittest.TestSuite()生成一个测试套件
# 通过使用addTest()方法将单个用例加入到套件
# 通过TextTestRunner()执行套件

# suite=unittest.TestSuite()
# suite.addTest(TestCalc("test_001"))

# 设计测试用例
class TestCalc(unittest.TestCase):
    def test_001(self):
        print("测试加法")
    def test_002(self):
        print("测试减法")
    def test_003(self):
        print("测试乘法")
    def test_004(self):
        print("测试除法")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()       # 生成一个测试套件的实例
    # 添加测试用例到套件中
    # 测试用例执行顺序是按照用例添加到套件的先后次序执行
    test_suite.addTest(TestCalc("test_001"))
    test_suite.addTest(TestCalc("test_003"))
    test_suite.addTest(TestCalc("test_002"))
    test_suite.addTest(TestCalc("test_004"))
    # 生成一个执行器的实例
    runner = unittest.TextTestRunner()
    # run方法执行测试套件
    runner.run(test_suite)