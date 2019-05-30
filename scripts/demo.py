from selenium.webdriver.common.by import By

from Base.getDriver import get_phone_driver
from Page.page import Page

driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
page_obj = Page(driver)

page_obj.get_home_page().click_my_btn()
page_obj.get_sign_page().click_sign()
page_obj.get_login_page().login("15800967928", "12345656")

toast = (By.XPATH, "//*[contains(@text,'错误')]")

result = page_obj.get_setting_page().get_element(toast, timeout=5, poll_frequency=0.5).text
print("toast：", result)
print("获取结果{}".format(page_obj.get_person_page().get_result()))

page_obj.get_person_page().click_setting_btn()
page_obj.get_setting_page().logout()
