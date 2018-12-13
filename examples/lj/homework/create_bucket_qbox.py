# -*- coding: utf-8 -*-

import os

from qiniu import Auth, http, urlsafe_base64_encode

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

q = Auth(access_key, secret_key)

bucket_name = 'tmp-1811282'
region = 'z0'
url = 'http://rs.qiniu.com/mkbucketv2/' + urlsafe_base64_encode(bucket_name) + '/region/' + region
data = ''
req = http._post_with_auth(url, data, q)
print (req[1])
