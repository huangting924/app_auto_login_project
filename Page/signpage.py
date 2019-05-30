from Base.Base import Base
from Page.UIElements import UIElements


class SignPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_sign(self):
        """点击已有账号 """
        self.click_element(UIElements.sign_exits_account_btn_id)
