#!/usr/bin/env python
import os

from qiniu import QiniuMacAuth
from qiniu import http

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

auth = QiniuMacAuth(access_key, secret_key)

url = 'http://ai.qiniuapi.com/v1/pulp'
data = {"data": {"uri": "http://7xlv47.com1.z0.glb.clouddn.com/pulpsexy.jpg"}}
req = http._post_with_qiniu_mac(url, data, auth)
print (req[0])
