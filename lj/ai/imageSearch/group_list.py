#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import qiniu
from qiniu import QiniuMacAuth
from qiniu import http

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

auth = QiniuMacAuth(access_key, secret_key)

url = 'http://ai.qiniuapi.com/v1/image/group'
data = {}
req = http._get_with_qiniu_mac(url, data, auth)
print (req[0])
