# coding:utf8
# python是动态脚本语言；不用写分号，靠缩进解析；不用声明数据类型;用%xx定义输出类型，%变量指定；

# 好习惯：全局变量；try,Exception;字典做参数；函数返回值；模块做对象；文档和注释

import random
import globals  # 包含globals包
import docstrings  # 包括文档字符串包
import getinfo
import sys

# 定义类型，不用声明数据类型，是弱类型
int_var = 5

# 打印
print "这是print打印"
print "16进制0x11:%d" % 0x11
print "16进制0x11:%d" % int_var

# 函数和数学计算
def operator(a, b):
    print "指数：%d" % (a ** b)
    # print "异或：%d" % (a ^ b)
    print "取模：%d" % (a % b)
    print "指数：%d" % pow(a, b)
    # print "浮点除：%d" % (a // b)
    # print "左移：%d" % (2 << 2)  # 2左移2位

# 调用函数
operator(2, 8)

# 帮助
# help(operator)
# help(int_var)

# 列表
aListxx = []
aListxx.append(4)
aListxx.append(55.55)
aListxx.append('a short string')
# aList.append(random.random) #这个显示地址
aListxx.append(random.random() * 10)

aList2 = [1, 2, 3, 4, 5]
aList3 = [6, 7, 8, 9, 10]

print aListxx
print aList2 + aList3

# 字典
dobj = {0: "zero", 1: "one", 2: "three", "liujing": "刘靖"}
print dobj[1], dobj['liujing'], dobj.get(2), dobj.get('liujing')

# 判断操作
if 1 in aList2:
    print "aList2 contain 1"
else:
    print "aList2 not contain 1"


a=1100
# elif
if a>=5:
    print('a>=5')
else:
    print('a<5')


print "转义字符\\n换行"

# 包含模块与全局变量
# help(globals)
globals.function1()
globals.function2()

# 查看文档字符串，使用“”“ XXX”“”对方法，类等进行描述
help(docstrings)

# 输入输出
# getinfo.ask()

# 显示命令行参数，文件路径
# print "文件路径与长度:%s,%d" % (sys.argv, len(sys.argv))
# i = 1
# for arg in sys.argv:
# 	print "%d, %s"%(i,arg)
# 	i += 1

# 文件操作，创建，写入，捕获异常
fname = "testpy.txt"
fmode = "wr" # write, read
f = open(fname, fmode)  # 打开文件
try:
    f.write("hello python\n你好 python")
    # print >> f, fname #写入fname的数据
    # lines = f.readlines()
    # for line in lines
    # 	print line
    pass
except Exception, e: # catch
    raise
else:
    pass
finally:
    f.close()
    pass

f = open("testpy.txt", "r")
lines = f.readlines()  # 读取全部内容
# for line in lines#读这个报错，坑爹
print lines

for i in range(1, 28 + 1):
    if pow(i, 85) % 35 == 6:  # i的85次方
        print i
        pass
