# coding=utf-8
# temp.py

# print pow(15,6)%9


# print 826 * 738

p = 827
q = 739
n = 611153
d = 186317  # d是下面的那个循环得出来的，直接使用就可以了
e = 65537
t = (p - 1) * (q - 1)
d = 0
for item in xrange(10506190, n):
    print item
    if e * item % t == 1:
        d = item
    break

M = u'中'  # 传送的值
M = ord(M)
# M = 2771
print '加密前的值：%s' % M
c = M ** d % n
print '加密后的值c:%s' % c

m = c ** e % n  # 解密后的值
print '解密后的值m:%s' % unichr(m).encode('utf-8')
