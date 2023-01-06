# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''

# 编辑成员信息页面
from appium.webdriver.common.mobileby import MobileBy
from APP_UI.BasePages.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phonenum):
        # input name
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text,'姓名')]/../android.widget.EditText", name)
        # input phonenum
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text,'手机')]/..//android.widget.EditText", phonenum)
        # click save
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        # 循环导入：全局导入会报错，改成局部导入
        from APP_UI.ModulesPages.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)