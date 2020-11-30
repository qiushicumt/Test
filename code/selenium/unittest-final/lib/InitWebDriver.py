from ReadConfig import ReadConfig
from selenium import webdriver
class InitWebDriver:
    """
    初始化webriver，并打开网站首页
    """
    def __init__(self):
        config = ReadConfig()
        chromedriver = config.get_config('chromedriver')
        url = config.get_config('url')
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(10)
        self.driver.get(url)
    def returnWebDriver(self):
        """
        返回webdriver对象
        :return: webdriver
        """
        return self.driver

