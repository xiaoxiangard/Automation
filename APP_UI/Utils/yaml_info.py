# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__：wangxiaoxiang
"""
import yaml


# 处理yaml数据
class YamlInfo:

    # 定义类方法，不用再去实例化
    @classmethod
    def read_info(cls):
        # 读取yaml数据
        with open('../Data/Mulator.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        return data
