# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__��wangxiaoxiang
"""
from faker import Faker


# mock��������
class GenerateInfo:
    # �����෽����������ȥʵ����
    @classmethod
    def get_name(cls):
        # ��������
        return Faker("zh_CN").name()

    @classmethod
    def get_phonenum(cls):
        # �����ֻ�����
        return Faker("zh_CN").phone_number()
