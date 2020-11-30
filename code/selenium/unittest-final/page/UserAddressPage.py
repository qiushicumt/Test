from BasePage import  BasePage
import  time
class UserAddressPage(BasePage):
    """
    收货地址page
    """
    def click_add(self):
        """
        点击按钮 "新增新地址"
        :return:None
        """
        self.by_css(".am-icon-plus").click()
        time.sleep(1)
        self.switch_frame(self.by_css("iframe[src*='saveinfo']"))

    def input_name(self,name):
        """
        输入姓名
        :return:None
        """
        self.by_css("input[name='name']").send_keys(name)

    def input_tel(self,tel):
        """
        输入电话号码
        :param tel: 电话号码
        :return: None
        """
        self.by_css("input[name='tel']").send_keys(tel)

    def choose_province(self,province):
        """
        选择省份
        :param province: 省份
        :return: None
        """
        self.by_css("select[name='province']+div").click()
        time.sleep(1)
        self.by_xpath("//*[@class='chosen-results']/li[text()='{}']".format(province)).click()
        time.sleep(1)
    def choose_city(self,city):
        """
        选择城市
        :param city:城市
        :return:None
        """
        self.by_css("select[name='city']+div").click()
        time.sleep(1)
        self.by_xpath("//*[@class='chosen-results']/li[text()='{}']".format(city)).click()
        time.sleep(1)
    def choose_county(self,county):
        """
        选择地区
        :param county: 地区
        :return: None
        """
        self.by_css("select[name='county']+div").click()
        time.sleep(1)
        self.by_xpath("//*[@class='chosen-results']/li[text()='{}']".format(county)).click()
        time.sleep(1)

    def input_address(self,address):
        """
        输入详细地址
        :param address: 详细地址
        :return: None
        """
        self.by_id("form-address").send_keys(address)
        time.sleep(3)

    def click_save(self):
        """
        点击保存
        :return: None
        """
        self.by_css("*[name='id']+button").click()
        time.sleep(1)

    def get_prompt(self):
        """
        获取提示
        :return: None
        """
        return self.by_css("#common-prompt p").text