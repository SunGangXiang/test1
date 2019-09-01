#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
import pytest
import time
import yaml

@pytest.fixture()
def cl():
    d = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "emulator-5554",
        "appPackage": "com.tencent.mobileqq",
        "appActivity": ".activity.SplashActivity",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "noReset": "true"
    }

    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
    time.sleep(8)
    return dr


@pytest.fixture()
def ml():
    with open(file=r"E:\APP自动化\QQ\element\login.yaml",mode="r",encoding="utf-8")as fb:
        p = yaml.load(fb,Loader=yaml.FullLoader)
    return p

@pytest.fixture()
def wo():
    a = {
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "emulator-5554",
      "appPackage": "com.alltuu.android",
      "appActivity": "android.alltuu.com.newalltuuapp.home.HomeActivity",
      "unicodeKeyboard": "true",
      "resetKeyboard": "true",
      "noReset": "true"
    }
    tu = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=a)
    time.sleep(8)
    return tu

@pytest.fixture()
def wty():
    with open(file=r"E:\APP自动化\QQ\element\wotuyun.yaml",mode="r",encoding="utf-8")as fm:
        w = yaml.load(fm,Loader=yaml.FullLoader)
    return w