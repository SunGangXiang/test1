#!/usr/bin/python
#-*-coding:utf-8-*-
# with open(file=r"E:\APP自动化\QQ\1.txt", mode="r", encoding="utf-8")as uu:
#     hh = uu.read().split(";")
#     f = []
#     for i in hh:
#         f.append(tuple(i.replace("\n","").split(",")))


# with open(file=r"E:\APP自动化\QQ\1.txt", mode="r", encoding="utf-8")as iu:
#     h = iu.read()
#     x = h.replace("\n", ",")
#     z = x.split(",")

with open(file=r"E:\APP自动化\QQ\3.txt", mode="r", encoding="utf-8")as uuu:
    hhh = uuu.read().split(";")
    ff = []
    for i in hhh:
        ff.append(tuple(i.replace("\n","").split(",")))
