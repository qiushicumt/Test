from selenium import webdriver
import  unittest
import  time
class Test_login(unittest.TestCase):
    """登陆模块"""
    @classmethod
    def setUpClass(cls) -> None:
        time.sleep(5)
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://localhost/shopxo/index.php?s=/index/user/logininfo.html")
        cls.driver=driver  #类变量被所有实例所共享

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.quit()

    def setUp(self) -> None:
        time.sleep(5)

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.refresh()  #清除输入内容

    def test_001(self):
        """验证输入错误的用户名"""
        self.driver.find_element_by_name("accounts").send_keys("test1")
        self.driver.find_element_by_name("pwd").send_keys("123456")
        self.driver.find_element_by_css_selector(".am-form.form-validation").submit()
        time.sleep(1)
        result=self.driver.find_element_by_css_selector("#common-prompt p").text
        self.assertEqual(result,"帐号不存在")

    def test_002(self):
        """验证输入正确的用户，错误的密码"""
        self.driver.find_element_by_name("accounts").send_keys("test01")
        self.driver.find_element_by_name("pwd").send_keys("1234567")
        self.driver.find_element_by_css_selector(".am-form.form-validation").submit()
        time.sleep(1)
        result=self.driver.find_element_by_css_selector("#common-prompt p").text
        self.assertEqual(result,"密码错误")

if __name__=='__main__':
    unittest.main(verbosity=2)