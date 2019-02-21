# -*- coding: utf-8 -*-
"""
获取指定域名指定时间内的日志链接
"""
import qiniu
import os
from qiniu import CdnManager

# 账户ak，sk
access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')
bucket_name = os.getenv('QINIU_TEST_BUCKET')

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

log_date = '2018-08-21'

urls = [
    'crawler-pub.iamlj.com'
]


ret, info = cdn_manager.get_log_list_data(urls, log_date)

print(ret)
print(info)
