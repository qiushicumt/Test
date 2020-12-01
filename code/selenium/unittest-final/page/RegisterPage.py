#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:RegisterPage.py
@time:2020/11/30
"""
import time
from BasePage import BasePage

class RegisterPage(BasePage):       # 继承BasePage

    def input_username(self, username):
        '''
        输入注册的用户名
        :param username：     传入的用户名
        :return:                不返回
        '''
        self.by_name("accounts").send_keys(username)

    def input_password(self, password):
        '''
        输入注册的密码
        :param password:    传入的密码
        :return:            不返回
        '''
        self.by_name("pwd").send_keys(password)

    def click_agreement(self):
        '''
        点击同意注册协议
        :return:            不返回
        '''
        self.by_css(".form-validation-username .am-icon-checked").click()

    def click_register(self):
        '''
        点击注册按钮
        :return:            不返回
        '''
        self.by_css(".form-validation-username").submit()

    def get_prompt(self):
        '''
        获取提示信息
        :return:        返回提示信息
        '''
        msg = self.by_css("#common-prompt p").text
        while msg == '':
            time.sleep(0.25)
            msg = self.by_css("#common-prompt p").text
        return msg

# if __name__ == '__main__':
#     pass
