# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__：wangxiaoxiang
"""
import logging
from APP_UI.BasePages.app import App
from APP_UI.Utils.generate_info import GenerateInfo


class TestContact:

    def setup_class(self):
        # 启动app
        self.app = App()

    def setup(self):
        self.main = self.app.start().go_main()

    def teardown_class(self):
        # 关闭app
        self.app.stop()

    def test_addcontact(self):
        name = GenerateInfo.get_name()
        phonenum = GenerateInfo.get_phonenum()
        logging.info(f"添加联系人姓名: {name}, 添加联系人手机号码: {phonenum} ")
        # 进入通讯录页面->点击添加成员->进入添加成员页面->输入成员信息->点击保存->获取结果
        result = self.main.goto_addresslist().click_addmember().\
            addmember_menual().edit_member(name, phonenum).get_result()
        assert "添加成功" == result

    def test_addcontact2(self):
        name = GenerateInfo.get_name()
        phonenum = GenerateInfo.get_phonenum()
        logging.info(f"添加联系人姓名: {name}, 添加联系人手机号码: {phonenum} ")
        # 进入通讯录页面->点击添加成员->进入添加成员页面->输入成员信息
        result = self.main.goto_addresslist().click_addmember().\
            addmember_menual().edit_member(name, phonenum).get_result()
        assert "添加成功" == result
