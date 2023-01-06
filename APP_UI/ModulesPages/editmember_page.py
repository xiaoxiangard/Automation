# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''

# �༭��Ա��Ϣҳ��
from appium.webdriver.common.mobileby import MobileBy
from APP_UI.BasePages.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phonenum):
        # input name
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text,'����')]/../android.widget.EditText", name)
        # input phonenum
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text,'�ֻ�')]/..//android.widget.EditText", phonenum)
        # click save
        self.find_and_click(MobileBy.XPATH, "//*[@text='����']")

        # ѭ�����룺ȫ�ֵ���ᱨ���ĳɾֲ�����
        from APP_UI.ModulesPages.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)