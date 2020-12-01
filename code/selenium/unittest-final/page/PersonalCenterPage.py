from BasePage import BasePage
import time
class PersonalCenterPage(BasePage):
    """
    个人中心首页 page
    """
    def into_MyAddress(self):
        """
        进入我的地址page
        :return: None
        """
        self.by_css("#collapse-nav-base a[href*='useraddress']").click()
        time.sleep(1)

    def into_MyInformation(self):
        """
        进入个人资料page
        :return: None
        """
        self.by_css("#collapse-nav-base a[href*='personal']").click()
        time.sleep(1)