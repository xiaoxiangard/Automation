# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__��wangxiaoxiang
'''
import logging
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException

class BasePage:
    #driver: WebDriver ����м�������ע�ͣ������п�������ʹ��
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(f"��λ��:{by}, ��λ���ʽ: {locator}")
        #����Ԫ��
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info(f"�������:")
        #�ҵ�Ԫ�ز����
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        logging.info(f"�������,��������Ϊ: {text}")
        #�ҵ�Ԫ�ز�����
        self.find(by, locator).send_keys(text)

    def swipe_find(self, by, locator, num=3):
        #ѭ�����β���
        for i in range(num):
            try:
                ele = self.find(by, locator)
                return ele
            except:
                #��������
                #��ȡ��Ļ�ߴ� 'width' 'height'
                size = self.driver.get_window_size()
                #��Ļ��
                width = size.get("width")
                #��Ļ��
                height = size.get("height")
                #���x
                start_x = width/2
                #���y
                start_y = height*0.8
                #�յ�x
                end_x = start_x
                #�յ�y
                end_y = height*0.2
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num - 1:
                raise NoSuchElementException(f"����{num}�Σ�δ�ҵ�")

    def swipefind_and_click(self, by, locator):
        logging.info(f"�������Һ�������:")
        #�ҵ�Ԫ�ز����
        self.swipe_find(by, locator).click()

    def getattr(self, by, locator, attribute="text"):
        #��ȡ���
        return self.find(by, locator).get_attribute(attribute)