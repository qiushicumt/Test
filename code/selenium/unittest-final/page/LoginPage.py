from BasePage import BasePage
import time
class LoginPage(BasePage):
    """
    登陆Page
    """

    def input_username(self,username):
        """
        输入登录账号
        :param username: 登录账号
        :return: None
        """
        self.by_name('accounts').send_keys(username)

    def input_password(self,password):
        """
        输入密码
        :param password: 登录密码
        :return: None
        """
        self.by_name('pwd').send_keys(password)

    def click_login(self):
        """
        点击登录
        :return: None
        """
        self.by_css(".form-validation").submit()
        time.sleep(1)

    def get_prompt(self):
        """
        获取登录后提示
        :return: 提示
        """
        # return self.by_css('#common-prompt p').text
        message = self.by_css('#common-prompt p').text
        while message == '':
            time.sleep(0.5)
            message = self.by_css('#common-prompt p').text
        return message

