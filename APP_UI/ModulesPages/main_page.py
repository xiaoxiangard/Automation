# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''

#��ҳҳ��
from appium.webdriver.common.mobileby import MobileBy
from APP_UI.BasePages.base_page import BasePage
from APP_UI.ModulesPages.addresslist_page import AddressListPage

class MainPage(BasePage):

    def goto_addresslist(self):
        #����ͨѶ¼
        self.find_and_click(MobileBy.XPATH, "//*[@text='ͨѶ¼']")
        return AddressListPage(self.driver)