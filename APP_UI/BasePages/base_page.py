# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
'''
__author__：wangxiaoxiang
'''
import logging
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException

class BasePage:
    #driver: WebDriver 入参中加入类型注释，方法中可以正常使用
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(f"定位符:{by}, 定位表达式: {locator}")
        #查找元素
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info(f"点击操作:")
        #找到元素并点击
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        logging.info(f"输入操作,输入内容为: {text}")
        #找到元素并输入
        self.find(by, locator).send_keys(text)

    def swipe_find(self, by, locator, num=3):
        #循环三次查找
        for i in range(num):
            try:
                ele = self.find(by, locator)
                return ele
            except:
                #滑动操作
                #获取屏幕尺寸 'width' 'height'
                size = self.driver.get_window_size()
                #屏幕宽
                width = size.get("width")
                #屏幕高
                height = size.get("height")
                #起点x
                start_x = width/2
                #起点y
                start_y = height*0.8
                #终点x
                end_x = start_x
                #终点y
                end_y = height*0.2
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num - 1:
                raise NoSuchElementException(f"找了{num}次，未找到")

    def swipefind_and_click(self, by, locator):
        logging.info(f"滑动查找后点击操作:")
        #找到元素并点击
        self.swipe_find(by, locator).click()

    def getattr(self, by, locator, attribute="text"):
        #获取结果
        return self.find(by, locator).get_attribute(attribute)