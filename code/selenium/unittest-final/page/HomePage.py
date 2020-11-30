from BasePage import BasePage
import time
class HomePage(BasePage):
    """
    首页 page
    """
    def logout(self):
        """
        首页退出
        :return: None
        """
        self.by_css(".menu-hd a[href*='logout']").click()
        time.sleep(3)  #退出后等待3秒再次回到首页
    def into_loginPage(self):
        """
        进入到登录页面
        :return: None
        """
        self.by_css(".menu-hd a[href*='logininfo']").click()
        time.sleep(1)
    def into_registerPage(self):
        """
        进入注册页面
        :return: None
        """
        self.by_css(".menu-hd a[href*='reginfo']").click()
        time.sleep(1)
    def into_userCenter(self):
        """
        进入到个人中心
        :return: None
        """
        self.by_css(".top-nav-right a[href*='user/index.html']").click()
        time.sleep(1)