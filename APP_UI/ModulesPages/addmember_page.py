# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''

#��ӳ�Աҳ��
from appium.webdriver.common.mobileby import MobileBy
from APP_UI.BasePages.base_page import BasePage


class AddMemberPage(BasePage):

    def addmember_menual(self):
        #�ֶ���ӳ�Ա��Ϣ
        self.find_and_click(MobileBy.XPATH, "//*[@text='�ֶ��������']")
        # ѭ�����룺ȫ�ֵ���ᱨ���ĳɾֲ�����
        from APP_UI.ModulesPages.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

    def get_result(self):
        #��ȡ���
        result = self.getattr(MobileBy.XPATH, "//*[@class='android.widget.Toast']", "text")
        return result
