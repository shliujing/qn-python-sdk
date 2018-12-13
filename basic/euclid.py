# coding:utf8
# euclid.py

__author__ = 'lj'


"""文档注释"""
# 单行注释

def gcd(a, b):
    if abs(a) < abs(b):
        return gcd(b, a)

    while abs(b) > 0:
        q,r = divmod(a,b)
        a,b = b,r
    return a

print gcd(4,10)

def extendedEuclideanAlgorithm(a, b):
    if abs(b) > abs(a):
        (x, y, d) = extendedEuclideanAlgorithm(b, a)
        return (y, x, d)

    if abs(b) == 0:
        return (1, 0, a)
    x1, x2, y1, y2 = 0, 1, 1, 0

    while abs(b) > 0:
        q, r = divmod(a, b)
        x = x2 - q * x1
        y = y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y

    return (x2, y2, a)


print extendedEuclideanAlgorithm(33, 44)
