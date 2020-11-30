from selenium import webdriver
import  unittest
import  time
from ddt import file_data,unpack,ddt,data
#page导入
from BasePage import BasePage
from HomePage import HomePage
from LoginPage import  LoginPage
from UserAddressPage import UserAddressPage
from PersonalCenterPage import PersonalCenterPage
#lib导入
from ReadConfig import  ReadConfig
from InitWebDriver import InitWebDriver

import logging
@ddt
class Test_UserAddress(unittest.TestCase):
    """
    资料管理->收货地址
    """
    @classmethod
    def setUpClass(cls) -> None:
        #初始化webdriver，并打开网站首页
        logging.info("------------------------------------------------------------------------------")
        logging.info("测试模块：用户地址")
        logging.info("打开首页")
        cls.driver=InitWebDriver().returnWebDriver()
        time.sleep(5)
        #进入登录页面
        logging.info("进入登录页面")
        homepage=HomePage(cls.driver)
        homepage.into_loginPage()
        #登录
        logging.info("登录")
        loginpage=LoginPage(cls.driver)
        loginpage.input_username("test01")
        loginpage.input_password("123456")
        loginpage.click_login()
        #进入个人中心-我的地址
        logging.info("进入我的地址")
        homepage.into_userCenter()
        personalcenterpage=PersonalCenterPage(cls.driver)
        personalcenterpage.into_MyAddress()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        logging.info("关闭浏览器")
        cls.driver.quit()
    def setUp(self) -> None:
        time.sleep(5)
    def tearDown(self) -> None:
        time.sleep(5)

    @file_data('userAddress.json')
    def test_add(self,name,tel,province,city,county,address,result):
        """添加收货地址"""
        logging.info("测试case:添加收货地址")
        useraddresspage=UserAddressPage(self.driver)
        useraddresspage.click_add()
        useraddresspage.input_name(name)
        useraddresspage.input_tel(tel)
        useraddresspage.choose_province(province)
        useraddresspage.choose_city(city)
        useraddresspage.choose_county(county)
        useraddresspage.input_address(address)
        useraddresspage.click_save()
        if tel=='':
            useraddresspage.click_save()
        self.assertEqual(useraddresspage.get_prompt(),result)

if __name__=='__main__':
    unittest.main(verbosity=2)