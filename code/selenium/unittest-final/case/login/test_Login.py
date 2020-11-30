from selenium import webdriver
import  unittest
import  time
from parameterized import parameterized
#page 导入
from BasePage import BasePage
from LoginPage import LoginPage
from HomePage import HomePage
#lib 导入
from ReadConfig import  ReadConfig
from InitWebDriver import InitWebDriver

import  logging
class Test_Login(unittest.TestCase):
    """登陆模块"""
    @classmethod
    def setUpClass(cls) -> None:
        logging.info("------------------------------------------------------------------------------")
        logging.info("测试模块：登录")
        logging.info("打开首页")
        #初始化webdriver，并打开网站首页
        cls.driver=InitWebDriver().returnWebDriver()
        time.sleep(5)

        # 进入登录页面
        logging.info("进入登录页面")
        homepage = HomePage(cls.driver)
        homepage.into_loginPage()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        logging.info("关闭浏览器")
        cls.driver.quit()  #关闭浏览器

    def setUp(self) -> None:
        time.sleep(5)

    def tearDown(self) -> None:
        time.sleep(5)
        logging.info("刷新")
        self.driver.refresh()  #清除输入内容

    #parameterized 数据驱动
    @parameterized.expand(
        [('case1','test1','123456','帐号不存在'),  #错误用户名
         ('case2', 'test01', '123456', '登录成功'),#正确用户名和密码
         ('case3','test01','1234567','密码错误') #正确用户名，错误密码

         ]
    )

    def test_login(self,case,username,password,result):
        """登录"""
        logging.info("测试case：登录")
        loginpage=LoginPage(self.driver)
        loginpage.input_username(username)
        loginpage.input_password(password)
        loginpage.click_login()
        self.assertEqual(loginpage.get_prompt(),result)

        if result=='登录成功':
            homepage=HomePage(self.driver)
            homepage.logout()
            homepage.into_loginPage()

if __name__=='__main__':
    unittest.main(verbosity=2)