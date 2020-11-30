from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    """
    封装selenium的常用方法
    目前已经封装方法如下：
    open 打开网站
    by_id id定位           bys_id id(s)定位
    by_css css定位        bys_css css(s)定位
    by_xpath xpath定位     bys_xpath xpath(s)定位
    by_name name定位      bys_name name(s)定位
    switch_frame 根据WebElement对象切换frame
    by_class class定位  bys_class class(s)定位
    """
    def __init__(self,driver):
        self.driver=driver

    def open(self,url):
        """
        打开测试网站
        :param url: 网站url地址
        :return: None
        """
        self.driver.get(url)

    def by_id(self,id):
        """
        id选择元素
        :param id: id选择器
        :return: WebElement对象
        """
        return self.driver.find_element_by_id(id)

    def bys_id(self,id):
        """
        id定位一组元素
        :param id: id选择器
        :return: WebElement对象的列表
        """
        return self.driver.find_elements_by_id(id)

    def by_css(self,css):
        """
        css选择元素
        :param css: css选择器
        :return: WebELement对象
        """
        return self.driver.find_element_by_css_selector(css)

    def bys_css(self,css):
        """
        css选择一组元素
        :param css: css选择器
        :return: WebElement对象的列表
        """
        return self.driver.find_elements_by_css_selector(css)

    def by_xpath(self,xpath):
        """
        xpath选择元素
        :param xpath: xpath选择器
        :return: WebElement对象
        """
        return self.driver.find_element_by_xpath(xpath)

    def bys_xpath(self,xpath):
        """
        xpath选择一组元素
        :param xpath: xpath选择器
        :return: WebElement对象的列表
        """
        return self.driver.find_elements_by_xpath(xpath)

    def by_name(self,name):
        """
        name选择元素
        :param name: name属性
        :return: WebElement对象
        """
        return self.driver.find_element_by_name(name)

    def bys_name(self,name):
        """
        name选择一组元素
        :param name: name属性
        :return: WebElement对象的列表
        """
        return self.driver.find_elements_by_name(name)
    def switch_frame(self,webelement):
        """
        reference为webelement，切换frame
        :param webelement: WebElement对象
        :return: None
        """
        self.driver.switch_to.frame(webelement)
    def by_class(self,classname):
        """
        通过class name定位元素
        :param classname: 类名
        :return: WebElement对象
        """
        return self.driver.find_element_by_class_name(classname)
    def bys_class(self,classname):
        """
        通过class name定位一组元素
        :param classname: 类名
        :return: 列表
        """
        return self.driver.find_elements_by_class_name(classname)
    # def wait_element(self,selector,text,time,frequency=0.5):
    #     """
    #     css定位元素，设定超时时间和频率，轮询查收元素是否包含text
    #     :param selector:css选择器
    #     :param text：期望出现的文本
    #     :param time: 超时时间
    #     :param frequency: 频率，默认0.5
    #     :return: WebElement对象
    #     """
    #     return  WebDriverWait(self.driver, time, frequency).until(EC.text_to_be_present_in_element(('css selector',selector),text))
