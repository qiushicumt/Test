#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:test_register.py
@time:2020/11/30
"""
# 导入基础模块
from selenium import webdriver
import unittest
import time
from parameterized import parameterized

# 导入lib
from InitWebDriver import InitWebDriver
from ReadConfig import ReadConfig
from Random9Num import Random9Num
# 导入page
from HomePage import HomePage
from RegisterPage import RegisterPage
#导入日志模块
import logging

# 套用框架，测试注册模块
# 假设我们测试2个case
# case1：正确的用户名和密码注册
# case2：正确的用户名，密码小于6位

class Test_Register(unittest.TestCase):
    """注册模块"""
    # setUpClass在测试类的开始被执行
    # setUpClass中主要进行页面初始化，打开主页，进入注册页面的操作
    @classmethod
    def setUpClass(cls) -> None:
        logging.info("------------------------------------------------------------------------------")
        logging.info("测试模块：注册")
        logging.info("打开首页")
        # 初始化webdriver，并打开网站首页
        cls.driver = InitWebDriver().returnWebDriver()
        time.sleep(5)
        # 进入注册页
        logging.info("进入注册页")
        homepage = HomePage(cls.driver)     # 传入cls.driver，先实例化一个HomePage的对象
        homepage.into_registerPage()        # 调用into_registerPage()方法，进入注册页

    # tearDownClass 在测试类的结束被执行
    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        logging.info("结束测试，关闭浏览器")
        cls.driver.quit()

    # 在测试用例的开始被执行
    def setUp(self):
        time.sleep(3)

    # 在测试用例的结束被执行
    def tearDown(self):
        time.sleep(3)
        # logging.info("刷新")
        # self.driver.refresh()  # 清除输入内容
    # parameterized 数据驱动
    # 使用expand方法，在执行测试用例前编写测试参数
    @parameterized.expand(
        [('case1','test'+Random9Num().returnNum(),'123456', '注册成功'),        # 正确的用户名和密码
         ('case2','test'+Random9Num().returnNum(),'12','密码格式 6~18 个字符之间')       # 错误的密码
         ]
    )

    # 执行测试用例
    # test_register执行的内容为页面进入到注册页面后进行的操作
    # 主要为输入用户名、输入密码、同意协议和点击注册按钮
    def test_register(self,case,username,password,result):
        """注册"""
        logging.info("测试case：注册")
        register_page = RegisterPage(self.driver)       # 传入初始化的cls.driver
        register_page.input_username(username)
        register_page.input_password(password)
        register_page.click_agreement()
        register_page.click_register()
        # result = register_page.get_prompt()
        # 添加断言
        self.assertEqual(register_page.get_prompt(), result)
        if result == '注册成功':        # 注册成功后要退出登录
            homepage = HomePage(self.driver)
            homepage.logout()
            logging.info("退出登录")
            homepage.into_registerPage()


if __name__ == '__main__':
    unittest.main(verbosity=2)
