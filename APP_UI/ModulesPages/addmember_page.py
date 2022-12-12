# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''

#添加成员页面
from appium.webdriver.common.mobileby import MobileBy
from APP_UI.BasePages.base_page import BasePage


class AddMemberPage(BasePage):

    def addmember_menual(self):
        #手动添加成员信息
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        # 循环导入：全局导入会报错，改成局部导入
        from APP_UI.ModulesPages.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

    def get_result(self):
        #获取结果
        result = self.getattr(MobileBy.XPATH, "//*[@class='android.widget.Toast']", "text")
        return result
