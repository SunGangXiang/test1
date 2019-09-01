#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
import time
import pytest
from QQ.until.zdh import ff
from QQ.until.滑动 import *
from QQ.头部 import duqu
from QQ.until.mylog import get_log
log = get_log(filename="test_2.py")



class Testone(object):
    @pytest.fixture()
    def dengl(self,wo,wty):
        b = wo.find_elements_by_class_name(wty['zm'])
        b[0].send_keys("17826808915")
        b[1].send_keys("123456")
        wo.find_elements_by_class_name(wty['dl'])[5].click()
        time.sleep(6)

    @pytest.mark.parametrize("y1,y2", ff)
    def test_3(self,wo,wty,y1,y2):
        b = wo.find_elements_by_class_name(wty['zm'])
        log.info(f"输入的账号是:{y1}")
        b[0].send_keys(f"{y1}")
        log.info(f"输入的密码是:{y2}")
        b[1].send_keys(f"{y2}")
        wo.find_elements_by_class_name(wty['dl'])[5].click()
        time.sleep(10)
        try:
            a = wo.find_element_by_class_name(wty['sy'])
            assert a.text == "喔图云摄影"
            log.info(f"成功抓取{a.text}")
            wo.find_elements_by_class_name(wty['sc'])[9].click()
            time.sleep(2)
            e = wo.find_elements_by_class_name(wty['tc'])
            for i in range(len(e)):
                if i == 1:
                    e[i].click()
            time.sleep(2)
        except:
            f = wo.find_elements_by_class_name(wty['tk'])
            assert f[8].text == "《喔图服务条款》"
            log.info(f"成功抓取{f[8].text}")
        else:
            wo.find_elements_by_class_name(wty['zh'])[-1].click()
            wo.find_elements_by_class_name(wty['sz'])[9].click()
            wo.find_elements_by_class_name(wty['tuichu'])[-1].click()
            time.sleep(8)
            g = wo.find_elements_by_class_name(wty['tk'])
            assert g[8].text == "《喔图服务条款》"
            log.info(f"成功抓取{g[8].text}")


    def test_4(self,dengl,wo,wty):
        for i in range(5):
            wo.find_element_by_class_name(wty['yi']).click()
            wo.find_element_by_class_name(wty['fanhui']).click()
            swipe_left(wo)


    def test_5(self,wo,wty):
        wo.find_elements_by_class_name(wty['sc'])[9].click()
        h = wo.find_elements_by_class_name(wty['tc'])
        for i in range(len(h)):
            if i == 1:
                assert h[i].text == "退出"
        wo.find_elements_by_class_name(wty['xc'])[6].click()
        k = wo.find_elements_by_class_name(wty['xc'])
        k[10].click()










