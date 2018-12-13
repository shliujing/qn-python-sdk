# -*- coding: utf-8 -*-
"""
创建存储空间
"""
import os

from qiniu import Auth
from qiniu import BucketManager

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

bucket_name = 'tmp-181128'

# "填写存储区域代号  z0:华东, z1:华北, z2:华南, na0:北美"
region = 'z0'

ret, info = bucket.mkbucketv2(bucket_name, region)
print(info)
print(ret)
assert info.status_code == 200
