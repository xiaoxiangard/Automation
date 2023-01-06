# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__��wangxiaoxiang
"""
import logging
from APP_UI.BasePages.app import App
from APP_UI.Utils.generate_info import GenerateInfo


class TestContact:

    def setup_class(self):
        # ����app
        self.app = App()

    def setup(self):
        self.main = self.app.start().go_main()

    def teardown_class(self):
        # �ر�app
        self.app.stop()

    def test_addcontact(self):
        name = GenerateInfo.get_name()
        phonenum = GenerateInfo.get_phonenum()
        logging.info(f"�����ϵ������: {name}, �����ϵ���ֻ�����: {phonenum} ")
        # ����ͨѶ¼ҳ��->�����ӳ�Ա->������ӳ�Աҳ��->�����Ա��Ϣ->�������->��ȡ���
        result = self.main.goto_addresslist().click_addmember().\
            addmember_menual().edit_member(name, phonenum).get_result()
        assert "��ӳɹ�" == result

    def test_addcontact2(self):
        name = GenerateInfo.get_name()
        phonenum = GenerateInfo.get_phonenum()
        logging.info(f"�����ϵ������: {name}, �����ϵ���ֻ�����: {phonenum} ")
        # ����ͨѶ¼ҳ��->�����ӳ�Ա->������ӳ�Աҳ��->�����Ա��Ϣ
        result = self.main.goto_addresslist().click_addmember().\
            addmember_menual().edit_member(name, phonenum).get_result()
        assert "��ӳɹ�" == result
