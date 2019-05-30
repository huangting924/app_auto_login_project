from Page.homepage import HomePage
from Page.loginPage import LoginPage
from Page.signpage import SignPage
from Page.personpage import PersonPage
from Page.settingpage import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        """获取首页对象"""
        return HomePage(self.driver)

    def get_sign_page(self):
        """获取注册页面对象"""
        return SignPage(self.driver)

    def get_login_page(self):
        """获取登录页面对象"""
        return LoginPage(self.driver)

    def get_person_page(self):
        """返回个人中心对象"""
        return PersonPage(self.driver)

    def get_setting_page(self):
        """返回设置页面对象"""
        return SettingPage(self.driver)
