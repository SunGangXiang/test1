#!/usr/bin/python
#-*-coding:utf-8-*-
import allure
import pytest

# feature:标注测试用例是属于哪一个模块的
@allure.feature("模块一")
def test_2():
    assert 0 == 0

@allure.feature("模块一")
def test_3():
    assert 1 == 1



# story:对一个测试用例的详细描述
@allure.feature("模块二")
@allure.story("这是一个非常哇塞的用例")
def test_4():
    assert 1 == 11

@allure.feature("模块二")
@allure.story("这是一个非常lo的用例")
def test_5():
    """
    这是对函数的参数、返回值的一个注释
    就这个feel倍爽
    """
    # 测试用例的描述是通过，函数的注释来获取的
    assert 10 == 10


# 测试用例的优先级
"""
Allure中对严重级别的定义：
1、 Blocker级别：阻塞/中断缺陷（客户端程序无响应，无法执行下一步操作）
2、 Critical级别：严重/临界缺陷（ 功能点缺失）
3、 Normal级别：普通缺陷（数值计算错误）
4、 Minor级别：次要缺陷（界面错误与UI需求不符）
5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）

"""
# severity 用例的优先级
@allure.feature("模块三")
@allure.severity("Blocker")
def test_6():
    assert 1 == 1

@allure.feature("模块三")
@allure.severity("Critical")
def test_7():
    assert 1 == 1

@allure.feature("模块三")
@allure.severity("Normal")
def test_8():
    assert 1 == 1

@allure.feature("模块三")
@allure.severity("Minor")
def test_9():
    assert 1 == 1

@allure.feature("模块三")
@allure.severity(" Trivial")
def test_10():
    assert 1 == 1

# git -- svn  -- jenkins  --  执行python代码  --  报告  --  访问某个网站
# step  记录测试用例中的一些步骤，日志代码可以通过step记录到报告中
# isinstance(参数一，参数二)判断数据类型的类，参数一和参数二是否是同一个类型、是True、不是Flase
@allure.feature("模块四")
@allure.step("字符串相加：{0}，{1}")#测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    if not isinstance(str1,str):
        return f"{str1} 不是字符串类型的"
    if not isinstance(str2,str):
        return f"{str2} 不是字符串类型的"
    return str1 + str2

@allure.feature("模块四")
def test_11():
    str1 = "hello"
    str2 = "world"

    assert str_add(str1,str2) == "helloworld"

# issue和testcase
# 对issue 和 teatcase 生成一个网址


@allure.step("字符串相加：{0}，{1}")
#测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature('模块五')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'

with open(file=r'E:\APP自动化\QQ\2.jpg', mode='rb',encoding="utf-8")as fs:
    a = fs.read()
allure.attach('test_img', a, allure.attachment_type.jpg)