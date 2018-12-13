# coding:utf8
# rsatest.py

print "这是一个例子："
p = 7
q = 17
n = 119
e = 5
t = (p - 1) * (q - 1)
d = 0  # d是下面的那个循环得出来的，通过计算，我们可以得到是77

for x in xrange(1, n + 1):
    # print x
    if e * x % t == 1:
        d = x
        break
    pass

M = 19  # 明文
print '加密前的值M: %s' % M
C = M ** d % n
print '加密后的值C: %s' % C
m = C ** e % n  # 解密后的值
print '解密后的值m: %s' % m
