#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import qiniu
from qiniu import QiniuMacAuth
from qiniu import http

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

auth = QiniuMacAuth(access_key, secret_key)

groupId = '789'
url = 'http://ai.qiniuapi.com/v1/image/group/' + groupId + "/new";
data = { "data": [ { "uri": "http://pcd7w9q78.bkt.clouddn.com/1.jpg", "attribute": { "id": "1", "label": "label1", "desc": "desc1" } }, { "uri": "http://pcd7w9q78.bkt.clouddn.com/2.jpg", "attribute": { "id": "2", "label": "label2", "desc": "desc2" } } ] }
req = http._post_with_qiniu_mac(url, data, auth)
print (req[0])