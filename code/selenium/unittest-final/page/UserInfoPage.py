#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:UserInfoPage.py
@time:2020/12/01
"""
import time
from BasePage import BasePage

class UserInfoPage(BasePage):
    """
    用户信息模块
    """
    # def nickname_clear(self):
    #     """
    #     清除用户昵称
    #     :return: None
    #     """
    #     self.by_name("nickname").clear()
    #     self.by_css(".form-validation legend").click()  # 清空后点击空白处

    def input_nickname(self, nickname):
        """
        输入用户昵称
        :param nickname: 用户昵称
        :return: None
        """
        self.by_name("nickname").clear()
        # time.sleep(0.5)
        self.by_name("nickname").send_keys(nickname)
        self.by_css(".form-validation legend").click()  # 清空后点击空白处
        time.sleep(0.5)


    def save_nickname(self):
        """
        保存昵称
        :return: None
        """
        self.by_css(".form-validation").submit()
        time.sleep(0.5)

    def get_prompt(self):
        """
        获取提示信息
        :return: msg提示信息
        """
        msg = self.by_css("#common-prompt p").text
        # while msg == '':
        #     time.sleep(0.5)
        #     msg = self.by_css("#common-prompt p").text
        return msg