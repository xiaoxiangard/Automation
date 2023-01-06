# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__：wangxiaoxiang
"""
# 专门放app相关操作
import logging
from appium import webdriver
from APP_UI.BasePages.base_page import BasePage
from APP_UI.ModulesPages.main_page import MainPage
from APP_UI.Utils.yaml_info import YamlInfo


class App(BasePage):
    # 启动
    def start(self):
        data = YamlInfo.read_info()
        if self.driver is None:
            logging.info(f"driver为:{self.driver}")
            # 初始化操作：打开应用
            self.desired_caps = data.get('mulatorsetcaps')
            address_set = data.get('addressset')[0]

            # 客户端和服务端建立连接
            self.driver = webdriver.Remote(address_set, self.desired_caps)
            # 隐式等待，每一次查找元素的时候，动态查找
            self.driver.implicitly_wait(40)
        else:
            # 启动app
            logging.info(f"复用 driver .")
            self.driver.start_activity(app_package=data['mulatorsetcaps']['appPackage'],
                                       app_activity=data['mulatorsetcaps']['appActivity'])
        return self

    # 停止
    def stop(self):
        self.driver.quit()

    # 重启
    def restart(self):
        data = YamlInfo.read_info()
        self.driver.terminate_app(app_id=data['mulatorsetcaps']['appPackage'])
        self.driver.start_activity(app_package=data['mulatorsetcaps']['appPackage'],
                                   app_activity=data['mulatorsetcaps']['appActivity'])

    # 跳转主页面
    def go_main(self):
        # 入口
        return MainPage(self.driver)
