#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:RegisterPage.py
@time:2020/11/30
"""
from BasePage import BasePage

class RegisterPage(BasePage):       # 继承BasePage

    def input_username(self, username):
        '''
        输入注册的用户名
        :param username：     传入的用户名
        :return:                不返回
        '''
        pass

    def input_password(self, password):
        '''
        输入注册的密码
        :param password:    传入的密码
        :return:            不返回
        '''
        pass

    def click_agreement(self):
        '''
        点击同意注册协议
        :return:            不返回
        '''
        pass

    def click_register(self):
        '''
        点击注册按钮
        :return:            不返回
        '''
        pass

    def get_prompt(self):
        '''
        获取提示信息
        :return:        返回提示信息
        '''
        pass

# if __name__ == '__main__':
#     pass
