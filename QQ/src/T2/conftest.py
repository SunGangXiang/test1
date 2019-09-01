#!/usr/bin/python
#-*-coding:utf-8-*-
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
import pytest
import time
import yaml

@pytest.fixture()
def wty():
    with open(file=r"E:\APP自动化\QQ\element\wb.yaml",mode="r",encoding="utf-8")as fm:
        q = yaml.load(fm,Loader=yaml.FullLoader)
    return q

@pytest.fixture()
def dl():
    dr = webdriver.Chrome()
    dr.set_window_position(380,0)
    return dr




