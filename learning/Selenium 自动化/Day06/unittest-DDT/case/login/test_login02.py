from selenium import webdriver
import  unittest
import  time
from ddt import ddt,data,file_data,unpack

@ddt
class Test_login(unittest.TestCase):
    """登陆模块"""
    @classmethod
    def setUpClass(cls) -> None:
        time.sleep(5)
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://localhost/shopxo/index.php?s=/index/user/logininfo.html")
        cls.driver=driver


    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.quit()

    def setUp(self) -> None:
        time.sleep(5)

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.refresh()  #清除输入内容

    #参数化读取JSON文件
    @file_data('login_data.json')
    def test_login(self,username,password,result):
        """登陆功能"""
        self.driver.find_element_by_name("accounts").send_keys(username)
        self.driver.find_element_by_name("pwd").send_keys(password)
        self.driver.find_element_by_css_selector(".am-form.form-validation").submit()
        time.sleep(1)
        res=self.driver.find_element_by_css_selector("#common-prompt p").text
        self.assertEqual(res,result)

if __name__=='__main__':
    unittest.main(verbosity=2)