#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:Random3Num.py
@time:2020/12/01
"""
from random import randint
class Random3Num:
    """
    产生3个随机数，返回字符串
    """
    def return3Num(self):
        num = ''
        for i in range(3):
            num += str(randint(0,9))
        return num

if __name__ == '__main__':
    pass
