# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__：wangxiaoxiang
"""
# 通讯录页面
from appium.webdriver.common.mobileby import MobileBy
from APP_UI.BasePages.base_page import BasePage
from APP_UI.ModulesPages.addmember_page import AddMemberPage


class AddressListPage(BasePage):

    def click_addmember(self):
        # 添加成员,防止添加过多成员，使用滑动查找的方法
        self.swipefind_and_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return AddMemberPage(self.driver)