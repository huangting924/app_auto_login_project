from Base.Base import Base
from Page.UIElements import UIElements


class SettingPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, tag=1):
        """
        点击退出操作
        :param tag: 1:确认退出，0 取消
        :return:
        """
        # 滑动页面
        self.scroll_screen()
        self.click_element(UIElements.setting_logout_btn_id)
        if int(tag) == 1:
            # 点击确认退出按钮
            self.click_element(UIElements.setting_acc_quit_btn_id)
        else:
            # 点击取消按钮
            self.click_element(UIElements.setting_dis_quit_btn_id)
