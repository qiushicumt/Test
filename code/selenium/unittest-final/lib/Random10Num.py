#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:Random10Num.py
@time:2020/12/01
"""
from random import randint
class Random10Num:
    """
    生成10位随机数
    """
    def returnNum(self):
        num = ''
        for i in range(10):
            num += str(randint(0,9))
        return num

if __name__ == '__main__':
    pass
