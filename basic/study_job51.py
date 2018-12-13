# coding:utf8
# 这部分是在51job上学习的，http://www.jb51.net/article/926.htm
# The range() function
def rangetest():
    a = range(5, 10)
    print a
    a = range(-2, -7) # 非递增
    print a
    a = range(-7, -2)
    print a
    a = range(-2, -11, -3)  # The 3rd parameter stands for step
    print a
    pass


# rangetest()


# 字符串访问
def stringtest():  # 截取不同的长度
    word = "abcdefg"
    a = word[2]
    print "a is: " + a
    b = word[1:3]
    print "b is: " + b  # index 1 and 2 elements of word.
    c = word[:2]
    print "c is: " + c  # index 0 and 1 elements of word.
    d = word[0:]
    print "d is: " + d  # All elements of word.
    e = word[:2] + word[2:]
    print "e is: " + e  # All elements of word.
    f = word[-1]
    print "f is: " + f  # The last elements of word.
    g = word[-4:-2]
    print "g is: " + g  # index 3 and 4 elements of word.
    h = word[-2:]
    print "h is: " + h  # The last two elements.
    i = word[:-2]
    print "i is: " + i  # Everything except the last two characters
    l = len(word)
    print "Length of word is: " + str(l)


# stringtest()

def listtest():
    word = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    a = word[2]
    print "a is: " + a
    b = word[1:3]
    print "b is: "
    print b  # index 1 and 2 elements of word.
    c = word[:2]
    print "c is: "
    print c  # index 0 and 1 elements of word.
    d = word[0:]
    # print "d is: "
    print d  # All elements of word.
    e = word[:2] + word[2:]
    print "e is: "
    print e  # All elements of word.
    f = word[-1]
    print "f is: "
    print f  # The last elements of word.
    g = word[-4:-2]
    print "g is: "
    print g  # index 3 and 4 elements of word.
    h = word[-2:]
    print "h is: "
    print h  # The last two elements.
    i = word[:-2]
    print "i is: "
    print i  # Everything except the last two characters
    l = len(word)
    print "Length of word is: " + str(l)
    print "Adds new element"
    word.append('h')
    print word


# listtest()

# 文件读写
def wrfile():
    spath = "./testfile2.txt"
    f = open(spath, "w")  # Opens file for writing.Creates this file doesn't exist.
    f.write("First line 1.\n")
    f.writelines("First line 2.")

    f.close()

    f = open(spath, "r")  # Opens file for reading

    for line in f:
        print line

    f.close()
    pass


# wrfile()

# 错误和控制机制
def tryexcept():
    s = raw_input("Input your age:")
    if s == "":
        raise Exception("Input must no be empty.")

    try:
        i = int(s)
    except ValueError:
        print "Could not convert data to an integer."
    except:
        print "Unknown exception!"
    else:  # It is useful for code that must be executed if the try clause does not raise an exception
        print "You are %d" % i, " years old"
    finally:  # Clean up action
        print "Goodbye!"
    pass


# tryexcept()

## 对象（属性，方法）
## 人（身高/体重，吃/走/跳）

# 继承
def inherittest():
    class Base:
        def __init__(self):
            self.data = []

        def add(self, x):
            self.data.append(x)

        def addtwice(self, x):
            self.add(x)
            self.add(x)

    # Child extends Base
    class Child(Base):  # 继承，放入括号内即可
        def plus(self, a, b):
            return a + b

    oChild = Child()  # 实例化
    oChild.add("str1")
    print oChild.data  # 成员变量不用声明
    print oChild.plus(2, 3)

    oChild.addtwice("ss ")
    print oChild.data
    pass


inherittest()#类也可以放入方法中

# 导入，可以导函数
def importa():  # 这里我改成getinfo文件
    from getinfo import add_func  # Also can be : import getinfo

    print "Import add_func from module getinfo"
    print "Result of 1 plus 2 is: "
    print add_func(1, 2)  # If using "import a" , then here should be "a.add_func"

# importa()

# 如何让Python知道这个文件层次结构?很简单,每个目录都放一个名为_init_.py 的文件

# 总结： 你会发现这个教程相当的简单.许多Python特性在代码中以隐含方式提出,这些特性包括:Python不需要显式声明数据类型,关键字说明,字符串函数的解释等等.我认为一个熟练的程序员应该对这些概念相当了解,这样在你挤出宝贵的一小时阅读这篇短短的教程之后,你能够通过已有知识的迁移类比尽快熟悉Python,然后尽快能用它开始编程.
