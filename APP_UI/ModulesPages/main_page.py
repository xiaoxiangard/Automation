# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''

#首页页面
from appium.webdriver.common.mobileby import MobileBy
from APP_UI.BasePages.base_page import BasePage
from APP_UI.ModulesPages.addresslist_page import AddressListPage

class MainPage(BasePage):

    def goto_addresslist(self):
        #进入通讯录
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return AddressListPage(self.driver)