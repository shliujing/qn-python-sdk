#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入16进制，转成10进制
import sys
import datetime
import time

a = int("0x"+sys.argv[1], 0)
timeArray = time.localtime(a)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
r = '转成10进制：\n'+str(a)+'\n转成当前时间：\n' + otherStyleTime
print(r)