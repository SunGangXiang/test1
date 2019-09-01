#!/usr/bin/python
#-*-coding:utf-8-*-
# 喔图云
from selenium import webdriver
from time import sleep
import pytest
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from QQ.until.zdh import ff

class Testone(object):
    @pytest.fixture()
    def wy(self,dl,wty):
        dl.get(wty["wwz"])

    # def test_1(self,dl,wty):
    #     dl.get(wty["bwz"])
    #     sleep(2)
    #     dl.find_element_by_id("kw").send_keys("喔图云")
    #     dl.find_element_by_id("su").click()
    #     wait = ui.WebDriverWait(dl, 10)
    #     wait.until(lambda dl:dl.find_element_by_xpath(wty['dj'])).click()
    #     sleep(2)
    #     ss = dl.window_handles
    #     dl.switch_to.window(ss[-1])
    #     wait.until(lambda dl:dl.find_element_by_xpath(wty['bt']).is_displayed())
    #     assert dl.title == "喔图云摄影-照片即时摄影服务|智能图片直播平台"
    #     dl.quit()
    #
    # def test_2(self,dl,wty,wy):
    #     wait = ui.WebDriverWait(dl, 10)
    #     wait.until(lambda dl:dl.find_element_by_xpath(wty['bt']).is_displayed())
    #     assert dl.title == "喔图云摄影-照片即时摄影服务|智能图片直播平台"
    #     dl.quit()
    #
    # def test_3(self,dl,wty,wy):
    #     wait = ui.WebDriverWait(dl, 10)
    #     wait.until(lambda dl: dl.find_element_by_xpath(wty['denglu'])).click()
    #     a = wait.until(lambda dl:dl.find_element_by_xpath(wty['zh'])).text
    #     assert a == '没有账户？'
    #     dl.quit()

    def test_4(self, dl, wty, wy):
        wait = ui.WebDriverWait(dl, 10)
        e = ['anli', 'kfpt', 'xzzx', 'women']
        ee = ['leixing','fu','chong','yong']
        for i in range(len(e)):
            for j in range(len(ee)):
                wait.until(lambda dl: dl.find_element_by_xpath(wty[e[i]])).click()
                c = wait.until(lambda dl: dl.find_element_by_xpath(wty[ee[j]])).text
                assert c == "用图片传播价值" or "重新定义公关摄影，推动摄影技术变革" or "赋能摄影师   共享云摄影" or "活动类型"



    #
    # @pytest.mark.parametrize("y1,y2", ff)
    # def test_8(self,dl,wty,wy,y1,y2):
    #     wait = ui.WebDriverWait(dl, 10)
    #     wait.until(lambda dl: dl.find_element_by_xpath(wty['denglu'])).click()
    #     wait.until(lambda dl: dl.find_element_by_xpath(wty['zhanghao'])).send_keys(f"{y1}")
    #     wait.until(lambda dl: dl.find_element_by_xpath(wty['mima'])).send_keys(f"{y2}")
    #     wait.until(lambda dl: dl.find_element_by_xpath(wty['ljdl'])).click()
    #     try:
    #         b = wait.until(lambda dl:dl.find_element_by_xpath(wty['mingzi'])).text
    #         assert b == "祥云科技有限公司"
    #     except:
    #         a = wait.until(lambda dl: dl.find_element_by_xpath(wty['zh'])).text
    #         assert a == '没有账户？'
    #         dl.quit()
    #     else:
    #         dl.quit()




