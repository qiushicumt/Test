#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:frankzhong
@file:unit_readYaml_demo.py
@time:2020/12/03
"""
import yaml

def read_yaml():
    read_file = open("test_data.yaml", encoding="utf-8")
    read_data = yaml.load(read_file, Loader=yaml.FullLoader)
    for one in read_data:
        print(type(one))
        print(one)

if __name__ == '__main__':
    read_yaml()
