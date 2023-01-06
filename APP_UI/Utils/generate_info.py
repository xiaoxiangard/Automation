# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__：wangxiaoxiang
"""
from faker import Faker


# mock测试数据
class GenerateInfo:
    # 定义类方法，不用再去实例化
    @classmethod
    def get_name(cls):
        # 生成姓名
        return Faker("zh_CN").name()

    @classmethod
    def get_phonenum(cls):
        # 生成手机号码
        return Faker("zh_CN").phone_number()
