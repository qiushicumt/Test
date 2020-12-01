# 常规导入
from selenium import webdriver
import time
import unittest
from parameterized import parameterized
# page导入
from PersonalCenterPage import PersonalCenterPage
from PersonalInformationPage import PersonalInformationPage
from HomePage import HomePage
from LoginPage import LoginPage
from PersonalCenterPage import PersonalCenterPage
from UserInfoPage import UserInfoPage
# lib导入
from InitWebDriver import InitWebDriver
from Random3Num import Random3Num
from Random10Num import Random10Num

import logging

class Test_PersonalInformation(unittest.TestCase):
    """
    用户信息模块
    """
    @classmethod
    def setUpClass(cls) -> None:
        logging.info("=====================================")
        logging.info("用户信息模块")
        logging.info("打开浏览器，打开网站首页")
        cls.driver = InitWebDriver().returnWebDriver()      # InitWebDriver初始化以后打开浏览器并打开网站首页
        time.sleep(3)       # 打开首页以后，静止3秒

        logging.info("打开登录页")
        HomePage(cls.driver).into_loginPage()
        logging.info("用户登录")
        loginPage = LoginPage(cls.driver)
        loginPage.input_username("test02")
        loginPage.input_password("123456")
        loginPage.click_login()
        time.sleep(3)
        logging.info("进入用户中心")
        HomePage(cls.driver).into_userCenter()      # 从首页进入用户中心
        personalCenterPage = PersonalCenterPage(cls.driver)
        logging.info("进入个人资料")
        personalCenterPage.into_MyInformation()
        logging.info("进入用户信息")
        personalInformationPage = PersonalInformationPage(cls.driver)
        personalInformationPage.into_userInfo()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        logging.info("关闭浏览器")
        cls.driver.quit()       # 退出，关闭浏览器

    def setUp(self) -> None:
        time.sleep(2)

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.refresh()

    @parameterized.expand(
        [('case1', 'user'+Random3Num().return3Num(), '编辑成功'),
         ('case2', '', '昵称 2~16 个字符之间'),
         ('case3', 'a', '昵称 2~16 个字符之间')]
    )
    def test_nickname(self, case, nickname, result):
        """ 修改用户昵称 """
        logging.info("修改用户昵称")
        userInfoPage = UserInfoPage(self.driver)
        # userInfoPage.nickname_clear()
        userInfoPage.input_nickname(nickname=nickname)
        userInfoPage.save_nickname()
        result_msg = userInfoPage.get_prompt()
        self.assertEqual(result_msg, result)
        if result == '编辑成功':
            homepage = HomePage(self.driver)
            homepage.into_userCenter()
            personalCenterPage = PersonalCenterPage(self.driver)
            personalCenterPage.into_MyInformation()
            personalInformationPage = PersonalInformationPage(self.driver)
            personalInformationPage.into_userInfo()

if __name__ == 'main':
    unittest.main(verbosity=2)