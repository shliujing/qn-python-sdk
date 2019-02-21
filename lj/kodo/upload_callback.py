# -*- coding: utf-8 -*-
# flake8: noqa
import os

from qiniu import Auth, put_file, etag

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

q = Auth(access_key, secret_key)

bucket_name = os.getenv('QINIU_TEST_BUCKET')

key = 'test/1218/test.png'

#上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
policy = {
 'callbackUrl': 'http://practice.dandantuan.com/demo/qiniu/qiniu_sdk_notify.php',
 'callbackBody': 'filename=$(fname)&filesize=$(fsize)&key=$(key)&bucket=$(bucket)'
 }

token = q.upload_token(bucket_name, key, 3600, policy)

localfile = '/Users/jingliu/Desktop/what-is-python..png'

ret, info = put_file(token, key, localfile)
print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)

