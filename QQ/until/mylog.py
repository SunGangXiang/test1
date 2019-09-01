#!/usr/bin/python
#-*-coding:utf-8-*-
import logging
import datetime

# 日志文件夹/目录
LOG_DIR = "E:\\APP自动化\\QQ\\log\\"

# 获取当前时间
# 日期.txt
# 创建一个日志文件的名字
a = LOG_DIR + str(datetime.datetime.now().date()) + ".txt"

# logging ---> python定义日志的库
# 定义日志输出的格式
# asctime 当前时间
# msecs 多少多少秒
# levelname -4s日志等级 最大4级

formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S')

# logging的两张输出方式
# 第一种输出到pycharm控制台
c = logging.StreamHandler()
# 添加日志的样式
c.setFormatter(formatter)

# 第二种输出到文本里
w = logging.FileHandler(a,encoding="utf-8")
# 添加日志的样式
w.setFormatter(formatter)

# 写日志
def get_log(filename):
    # 获取执行日志的脚本名字
    l = logging.getLogger(filename)
    # 添加输出内容到控制台
    l.addHandler(c)
    # 添加输出内容到文本
    l.addHandler(w)
    # 定义日志的等级  INFO --> 最低等级:DEBUG  最高级：CRITICAL
    l.setLevel(logging.INFO)
    return l


# log = get_log()
# log.info("qwergthjk")
# log.error("qwertyui")
