#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:unittest_testloader.py
@time:2020/11/30
"""
import unittest

# 通过TestLoader类的loaderTestsFromTestCase()方法将测试用例一次性全部添加到测试套件中
# suite=unittest.TestLoader().loadTestsFromTestCase(TestCalc)

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
    # 通过loadTestsFromTestCase()方法直接加载测试用例的类，生成一个测试套件
    # 测试套件执行
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
