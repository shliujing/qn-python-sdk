# coding:utf8
# getinfo.py

# 命令行可以执行，但是sublime下会读取
def ask():
    name = raw_input("what is your name?")
    secname = raw_input("what is your secname?")

    print "so,your name is %s ,secname is %s" % (name, secname)
    ack = raw_input("is that right?(y/n)")
    print ack
    if ask in ('y', 'Y'):
        print "Cool!"
    else:
        print "OK,what ever"
    pass


def add_func(a, b):
    return a + b

if __name__ == '__main__':
    ask()
