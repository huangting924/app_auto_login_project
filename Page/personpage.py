from Base.Base import Base
from Page.UIElements import UIElements


class PersonPage(Base):
    """我的个人中心页面"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_result(self):
        """获取个人中心页面 我的优惠卷"""
        # timeout = 10, poll_frequency = 1.0
        return self.get_element(UIElements.person_shop_cart_id, timeout=10, poll_frequency=1.0).text

    def click_setting_btn(self):
        """点击设置按钮"""
        self.click_element(UIElements.person_setting_btn_id)
