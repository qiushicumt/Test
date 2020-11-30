from selenium import webdriver
class BasePage:
    """
    封装selenium的常用方法
    目前已经封装方法如下：
    open 打开网站
    by_id id定位           bys_id id(s)定位
    by_css css定位        bys_css css(s)定位
    by_xpath xpath定位     bys_xpath xpath(s)定位
    by_name name定位      bys_name name(s)定位
    by_class class定位
    """
    def __init__(self,driver):
        self.driver=driver  #实例变量
    def by_class(self,classname):
        """
        通过class定位元素
        :param classname: class名称
        :return: webelement对象
        """
        return self.driver.find_element_by_class_name(classname)

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