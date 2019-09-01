#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
import time
import pytest
from QQ.until.zdh import f
# from QQ.until.zdh import z
from selenium.common.exceptions import NoSuchElementException
from QQ.until.滑动 import *
from QQ.until.mylog import get_log
log = get_log(filename="test_1.py")


"""
class Test_1(object):
    @pytest.mark.parametrize("y1,y2",f)
    def test_2(self,cl,ml):
        time.sleep(5)
        # 最初登陆
        cl.find_element_by_id(ml['dian']).click()
        # time.sleep(6)
        输入账号
        cl.find_element_by_accessibility_id(ml['zh']).clear()
        cl.find_element_by_accessibility_id(ml['zh']).send_keys("1106589021")
        # 输入密码
        cl.find_element_by_id(ml['mima']).clear()
        cl.find_element_by_id(ml['mima']).send_keys("Sgx1106589021..+")
        cl.find_element_by_id(ml['denglu']).click()
        滑动
        time.sleep(2)
        swipe_up(cl)
        cl.find_element_by_xpath(ml['tou']).click()
        cl.find_element_by_id(ml['seting']).click()
        cl.find_element_by_id(ml['zhanghao']).click()
        cl.find_element_by_id(ml['tuihao']).click()
        cl.find_element_by_id(ml['quxiao']).click()
        cl.find_element_by_id(ml['tuihao']).click()
        cl.find_element_by_id(ml['tuichu']).click()
        t = cl.find_element_by_accessibility_id(ml['xinyonghu'])
        assert t.text == "用户注册"

    def test_3(self,cl,ml):
        for i in range(len(z)):
            cl.find_element_by_accessibility_id(ml['zh']).clear()
            cl.find_element_by_accessibility_id(ml['zh']).send_keys(f"{z[i]}")
            cl.find_element_by_id(ml['mima']).clear()
            cl.find_element_by_id(ml['mima']).send_keys(f"{z[i]}")
            cl.find_element_by_id(ml['denglu']).click()
            cl.find_element_by_id(ml['qd']).click()

    def test_4(self,cl,ml,y1,y2):
        cl.find_element_by_accessibility_id(ml['zh']).clear()
        log.info(f"账号是{y1}")
        cl.find_element_by_accessibility_id(ml['zh']).send_keys(f"{y1}")
        cl.find_element_by_id(ml['mima']).clear()
        log.info(f"密码是{y2}")
        cl.find_element_by_id(ml['mima']).send_keys(f"{y2}")
        cl.find_element_by_id(ml['denglu']).click()
        time.sleep(10)
        try:
            time.sleep(5)
            t = cl.find_element_by_accessibility_id(ml['xinyonghu'])
            assert t.text == "用户注册"

        except:
            time.sleep(5)
            r = cl.find_element_by_id(ml['qd'])
            assert r.text == "确定"

        try:
            time.sleep(5)
            v = cl.find_element_by_xpath(ml['xx'])
            assert v.text == "消息"
            cl.find_element_by_xpath(ml['tou']).click()
            cl.find_element_by_id(ml['seting']).click()
            cl.find_element_by_id(ml['zhanghao']).click()
            cl.find_element_by_id(ml['tuihao']).click()
            cl.find_element_by_id(ml['tuichu']).click()

        except:
    #         pass








# dr.find_element_by_class_name("android.widget.Button").click()
# time.sleep(2)
# dr.find_element_by_id("com.tencent.mobileqq:id/settings").click()
# time.sleep(1)
# dr.find_element_by_id("com.tencent.mobileqq:id/account_switch").click()
# dr.find_element_by_id("com.tencent.mobileqq:id/logoutBtn").click()
# dr.find_element_by_id("com.tencent.mobileqq:id/dialogLeftBtn").click()
# dr.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()

# 退出
# a = dr.find_elements_by_class_name("android.widget.RelativeLayout")
# for i in range(len(a)):
#
#     if i == 11:
#         a[i].click()
# dr.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()



    # x = h.replace("\n", ",")
    # # z = x.split(",")
    # d2 = [tuple(x.split(","))]
    # # @pytest.mark.parametrize("y1,y2",d2)
    # print(d2)
"""
