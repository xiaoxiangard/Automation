# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__��wangxiaoxiang
"""
# ͨѶ¼ҳ��
from appium.webdriver.common.mobileby import MobileBy
from APP_UI.BasePages.base_page import BasePage
from APP_UI.ModulesPages.addmember_page import AddMemberPage


class AddressListPage(BasePage):

    def click_addmember(self):
        # ��ӳ�Ա,��ֹ��ӹ����Ա��ʹ�û������ҵķ���
        self.swipefind_and_click(MobileBy.XPATH, "//*[@text='��ӳ�Ա']")
        return AddMemberPage(self.driver)