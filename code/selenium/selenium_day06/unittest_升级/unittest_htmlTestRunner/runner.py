#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:runner.py
@time:2020/11/30
"""
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

def test_runner():
    # 先获取文件根目录
    # os.path.abspath(__file__)获取的是当前runner.py文件的绝对路径
    # os.path.dirname()获取的是runner.py的根目录，即项目的根目录
    start_dir = os.path.dirname(os.path.abspath(__file__))

    # discover方式将测试用例添加到测试套件中
    # defaultTestLoader的discover方法，传入两个参数，返回测试套件实例对象
    # 第一个参数为：遍历查询的目录
    # 第二个参数为：查询的测试用例文件的文件名
    # 错误：test_suite = unittest.TestLoader().discover(start_dir, 'test*.py')
    test_suite = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern="test*.py")

    # 设置保存的测试报告的时间格式
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 以wb的方式打开测试报告文件，如果没有，则创建
    fp = open("./report/result_"+now+".html", "wb")

    runner = HTMLTestRunner(stream=fp, verbosity=2, title="ShopXO Test Report", description=None)
    runner.run(test_suite)
    fp.close()

if __name__ == '__main__':
    test_runner()
