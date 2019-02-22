#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import qiniu
from qiniu import QiniuMacAuth
from qiniu import http

access_key = '1oMhuZ5a7zjXSSMjM1KWQKGUpbCkEUw9yxYy1ENE'
secret_key = 'vnq9qhe_rrx4cBHUHOz0Mhz94ai5xAnYf_Pyunkj'

auth = QiniuMacAuth(access_key, secret_key)

url = 'http://ai.qiniuapi.com/v1/image/group'
data = {}
req = http._get_with_qiniu_mac(url, data, auth)
print(req[0])
