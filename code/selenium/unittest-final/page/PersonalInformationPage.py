#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:PersonalInformationPage.py
@time:2020/12/01
"""
import time
from BasePage import BasePage

# 继承BasePage
class PersonalInformationPage(BasePage):
    """ 用户资料模块 """
    def into_userInfo(self):
        """
        进入用户信息page
        :return: None
        """
        self.by_css(".user-content-body a[href*='personal']").click()
        time.sleep(1)