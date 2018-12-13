#!/usr/bin/env python
# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth
import os

import requests
import json

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

auth = QiniuMacAuth(access_key, secret_key)

url = 'http://ai.qiniuapi.com/v1/image/censor'
data = '{ "data": { "uri": "http://oayjpradp.bkt.clouddn.com/Audrey_Hepburn.jpg" }, "params": { "type": [ "pulp", "terror", "politician" ], "detail": true } }'

token = auth.token_of_request(method='POST', url=url, body=json.dumps(data), content_type='application/json',
                              qheaders="", host="ai.qiniuapi.com")
header = {'Content-Type': 'application/json', 'Authorization': 'Qiniu %s' % token}

req = requests.post(url, headers=header, data=json.dumps(data))

print (req.text)
print (req.status_code)
print(req.headers)
