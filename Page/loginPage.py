from Base.Base import Base
from Page.UIElements import UIElements


class LoginPage(Base):
    """登录页面"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, username, password):
        """登录"""
        # 账号
        self.send_element(UIElements.login_account_id, username)
        # 密码
        self.send_element(UIElements.login_passwd_id, password)
        # 登录按钮
        self.click_element(UIElements.login_btn_id)

    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(UIElements.login_close_btn)

    def if_login_btn(self):
        """获取登录按钮"""
        return self.get_element(UIElements.login_btn_id)

