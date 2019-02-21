# -*- coding: utf-8 -*-
# flake8: noqa

import os

from qiniu import Auth

# 生成私有 url

# 需要填写你的 Access Key 和 Secret Key 要上传的空间
access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

# 构建鉴权对象
q = Auth(access_key, secret_key)

# 生成私有 url
url = 'http://crawler-private.iamlj.com/1.png'
time = 3600
# 打印
private_url = q.private_download_url(url, time)

print private_url
