#encoding=utf-8
from  time import sleep

import pytest
import yaml
from appium import webdriver
class TestSearch():
    def setup_method(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '9'
        caps['deviceName'] = 'BGRNW20312000304'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['autoGrantPermissions'] = True
        caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
    def teardown_method(self):
        self.driver.quit()
        print(2)

    @pytest.mark.parametrize("a", yaml.safe_load(open("./search.yaml")))
    def test_search(self,a):
        self.driver.implicitly_wait(5)
        #点击搜索
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gq_")
        el2.click()
        #点击搜索框
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/ffq")
        el3.click()
        #输入搜索内容
        el3.send_keys(a)
        try:
            #点击搜索出来的第一个元素
            el4 = self.driver.find_element_by_id("com.tencent.wework:id/de1")
            el4.click()
            #点击输入框
            el5 = self.driver.find_element_by_id("com.tencent.wework:id/dtv")
            el5.click()
            el5.send_keys("你好")
        except Exception:

            print("请输入正确的联系人再搜索")
