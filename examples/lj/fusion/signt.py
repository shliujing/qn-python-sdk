# -*- coding: utf-8 -*-

from hashlib import md5
import urllib
import sys
import time
from urlparse import urlparse, parse_qs
import traceback
import uuid
import base64

# 命令示例 过期时间戳
# $ python signt.py time bfa860b8caa9c08aa7abccb888bb9dbaf8980aa8 http://i.iamlj.com/18-12-14/71187066.jpg 3600
# http://i.iamlj.com/18-10-24/98594789.jpg?sign=9f661ab14c97275fe67cccfdcf819526&t=5c1385e3


# $ python signt.py deadline bfa860b8caa9c08aa7abccb888bb9dbaf8980aa8 http://i.iamlj.com/18-10-24/98594789.jpg 1544780283
# http://i.iamlj.com/18-8-23/30787313.jpg?sign=1b1377b29d5735956b652d8ff5ebaa45&t=5c13837a

def url_encode(s):
    return urllib.quote(s.decode(sys.stdin.encoding).encode("utf8"), safe="/")


def to_deadline(rang):
    return int(time.time()) + rang


def t16(t):
    return hex(t)[2:].lower()  # 16 进制小写形式


def summd5(str):
    m = md5()
    m.update(str)
    return m.hexdigest()


def sign(key, t, path):
    a = key + url_encode(path) + t
    print("S: " + a)
    sign_s = summd5(a).lower()
    sign_part = "sign=" + sign_s + "&t=" + t
    return sign_part


def sign_url(key, t, p_url):
    url = urllib.unquote(p_url)
    up = urlparse(url)
    path = up.path
    sign_part = sign(key, t, path)
    p_query = up.query
    if p_query:
        query_part = "?" + p_query + "&" + sign_part
    else:
        query_part = "?" + sign_part

    return up.scheme + "://" + up.netloc + url_encode(path) + query_part


def printurl_encode_help():
    print '''
# 要求正确的 url_encode 编码，斜线 / 不编码；
# 井号 # 等在浏览器会直接识别为其它含义，若在 path 中必须编码；
# 问号 ? 等在 url 中有特殊含义，若在 path 中必须编码；
# 部分字符 "~!$&'()*+,:;=@[]" 不含双引号 "，虽有特殊含义，但在 path 部分，编码与否，都可以正常访问；
# 另一些，如 双引号 ", 空格 " ", 汉字等必须编码；
#
# 建议 url 的 path 中尽量不含上述部分，建议 url 中尽量不含上述部分。
#
# 参考
# https://www.wikiwand.com/zh-cn/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81
# https://www.wikiwand.com/en/Percent-encoding
# https://www.wikiwand.com/de/URL-Encoding
    '''


def signt_help():
    print
    print "./signt.py time <key> <url> <t,eg: 3600>"
    print "./signt.py deadline <key> <url> <deadline>"
    print "./signt.py check <key> <signed_url>"
    print "./signt.py show <t, eg: 55bb9b80>"
    print "./signt.py genkey"
    print "\n"
    print '''
# example:

# url = "http://xxx.yyy.com/DIR1/中文/vodfile.mp4?sfdf=dfe"
# key = 12345678
# 过期时间点: Sat Aug  1 00:00:00 2015  ==> 1438358400

# 执行: signt.py deadline 12345678  http://xxx.yyy.com/DIR1/中文/vodfile.mp4?sfdf=dfe 1438358400
# 签名 url 为: http://xxx.yyy.com/DIR1/%E4%B8%AD%E6%96%87/vodfile.mp4?sfdf=dfe&sign=6356bca0d2aecf7211003e468861f5ea&t=55bb9b80

# 执行: signt.py check 12345678 "http://xxx.yyy.com/DIR1/%E4%B8%AD%E6%96%87/vodfile.mp4?sfdf=dfe&sign=6356bca0d2aecf7211003e468861f5ea&t=55bb9b80"
# 显示: True
    '''
    print "\n"
    printurl_encode_help()


def sign_time(key, url, rang):
    print("range: " + str(rang))
    deadline = to_deadline(rang)
    sign_deadline(key, url, deadline)


def sign_deadline(key, url, deadline):
    print("\nkey: " + key)
    print("\nurl: " + url)
    print("\ndeadline: " + t16(deadline) + ", " + str(deadline) + ", " + time.ctime(deadline))
    print
    t = t16(deadline)
    signed_url = sign_url(key, t, url)
    print "\nsigned_url:"
    print signed_url
    print


# signed_url 是正确 url_encode 编码后签出的 url
# 见 url_encode 方法注释
def sign_check(key, signed_url):
    print "\n 要求: 待检测的 url 是正确 url_encode 编码后签出的 url"
    printurl_encode_help()
    u = urlparse(signed_url)
    t = parse_qs(u.query)["t"][0]
    sign_s = summd5(key + u.path + t).lower()
    print
    print("deadline: " + str(int(t, 16)) + " , " + time.ctime(int(t, 16)))
    print(sign_s)
    print(parse_qs(u.query)["sign"][0] == sign_s)


def show_t(t):
    i_t = int(t, 16)
    s_t = time.ctime(i_t)
    print(t + " : " + str(i_t) + " : " + s_t)


# 仅用于测试
def gen_key():
    print base64.urlsafe_b64encode(str(uuid.uuid4()))[:40].lower()


try:
    type = sys.argv[1]

    if type == "time":
        sign_time(sys.argv[2], sys.argv[3], int(sys.argv[4]))
    elif type == "deadline":
        sign_deadline(sys.argv[2], sys.argv[3], int(sys.argv[4]))
    elif type == "check":
        sign_check(sys.argv[2], sys.argv[3])
    elif type == "show":
        show_t(sys.argv[2])
    elif type == "genkey":
        gen_key()
    else:
        signt_help()
except Exception as e:
    print traceback.format_exc()
    signt_help()
