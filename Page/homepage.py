from Base.Base import Base
from Page.UIElements import UIElements


class HomePage(Base):
    """我的主页面"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_my_btn(self):
        """点击首页我的"""
        self.click_element(UIElements.home_my_btn_id)
