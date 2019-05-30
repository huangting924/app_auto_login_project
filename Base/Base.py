from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import allure


class Base:
    """base 基类 元素封装"""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=30, poll_frequency=1.0):
        """定位单个元素"""
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=30, poll_frequency=1.0):
        """定位一组元素"""
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """对元素的点击操作"""
        self.get_element(loc).click()

    def send_element(self, loc, text):
        """元素进行输入内容操作"""
        element = self.get_element(loc)
        element.clear()
        element.send_keys(text)

    def scroll_screen(self, sc=1):
        """
        滑动页面
        :param sc: sc：1向下2 2：向上 3向左 4向右
        :return:
        """
        time.sleep(3)
        # 获取屏幕的分辨率
        screen_size = self.driver.get_window_size()
        # 获取屏幕的宽
        width = screen_size.get("width")
        # 获取屏幕的高
        height = screen_size.get("height")
        if isinstance(sc, int):  # 判断是否是int类型
            if sc == 1:
                # 向上
                self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
            elif sc == 2:
                # 向下
                self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
            elif sc == 3:
                # 向左
                self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
            elif sc == 4:
                # 向右
                self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

        else:
            print("输入的不是整数！！！")

    def get_screen_page(self, name="图片"):
        """
        报告添加截图
        :param name: 截图的名称
        :return:
        """

        png_name = "./image/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)

        # 上传到测试用例中
        with open(png_name, "rb") as f:
            # 使用添加附件添加到 allure 报告
            allure.attach(name, f.read(), allure.attach_type.PNG)

    def get_page_toast(self, toast):
        """页面toast元素"""
        page_toast_xpath = (By.XPATH, "//*[contains(@text,'{}')]".format(toast))
        return self.get_element(page_toast_xpath, timeout=5, poll_frequency=0.5).text
