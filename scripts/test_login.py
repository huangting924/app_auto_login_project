import time

import pytest
import sys
import os
import yaml

sys.path.append(os.getcwd())
from Base.getDriver import get_phone_driver
from Page.page import Page
from Base.getfiledata import GetFileData
from selenium.common.exceptions import TimeoutException


def get_login_data():
    suc_list = []
    fail_list = []
    data = GetFileData().get_yaml_data("login_data.yaml")
    # print(data)
    for i in data:
        if data.get(i).get("toast"):
            # 逆向用例
            fail_list.append((i, data.get(i).get("account"), data.get(i).get("passwd"),
                              data.get(i).get("toast"), data.get(i).get("expect_data")))
        else:
            # 正向用列
            suc_list.append((i, data.get(i).get("account"), data.get(i).get("passwd"),
                             data.get(i).get("expect_data")))
    return {'suc': suc_list, 'fail': fail_list}


print(get_login_data())


class TestLogin:

    def setup_class(self):
        # 获取驱动对象
        self.driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        # 获取page 对象
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        # 关闭驱动对象
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def auto_in_login(self):
        # 点击首页我的按钮
        self.page_obj.get_home_page().click_my_btn()
        # 点击 注册 页已有账号登录
        self.page_obj.get_sign_page().click_sign()

    @pytest.mark.parametrize("case_num,account,passwd,expect_data", get_login_data().get("suc"))
    def test_login_success(self, case_num, account, passwd, expect_data):
        """正向测试用例"""
        # 调用login——page 中操作元素方法
        # 输入用户名 密码
        self.page_obj.get_login_page().login(account, passwd)
        try:
            shop_cart = self.page_obj.get_person_page().get_result()
            try:
                # 获取我的优惠券 断言
                assert expect_data == shop_cart
            except AssertionError:
                # 停留在个人中心页面，需要执行退出操作
                # 截图
                self.page_obj.get_login_page().get_screen_page()
                assert False
            finally:
                # 退出操作
                self.page_obj.get_person_page().click_setting_btn()
                self.page_obj.get_setting_page().logout()

        except TimeoutException:
            # 截图
            self.page_obj.get_login_page().get_screen_page("登录失败")
            # 点击退出 到首页
            self.page_obj.get_login_page().close_login_page()
            assert False

    @pytest.mark.parametrize("case_num,account,password,toast,expect_data", get_login_data()
                             .get("fail"))
    def test_login_fail(self, case_num, account, password, toast, expect_data):
        """逆向测试用例"""
        # 输入用户名密码
        self.page_obj.get_login_page().login(account, password)
        # 获取toast
        try:
            toast_text = self.page_obj.get_login_page().get_page_toast(toast)
            print("toast-----:", toast_text)
            try:
                # 判断登录按钮 是否存在
                self.page_obj.get_login_page().if_login_btn()
                assert toast_text == expect_data
            except TimeoutException:
                """获取到的toast错误提示信息，但是登录成功"""
                """个人中心页面"""
                # 截图
                self.page_obj.get_login_page().get_screen_page()
                # 登录按钮不在 个人中心 页面
                self.page_obj.get_person_page().click_setting_btn()
                self.page_obj.get_setting_page().logout()
                assert False

            except AssertionError:
                """登录页面"""
                # 截图
                self.page_obj.get_login_page().get_screen_page()
                # 关闭登录
                self.page_obj.get_login_page().close_login_page()
                assert False

        except TimeoutException:
            # 超时 获取不到toast 判断登录按钮
            self.page_obj.get_login_page().get_screen_page()
            try:
                """登录页面"""
                # 获取登录按钮
                self.page_obj.get_login_page().get_login_btn()
                # 则退出登录页面
                self.page_obj.get_login_page().close_login_page()

            except TimeoutException:
                """个人中心页面"""
                # 登录按钮不在 则点击个人中心设置，退出登录
                self.page_obj.get_person_page().click_setting_btn()
                self.page_obj.get_setting_page().logout()
            assert False
