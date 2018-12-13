# -*- coding: utf-8 -*-
# flake8: noqa
import hmac
import os
from hashlib import sha1

from qiniu import Auth, urlsafe_base64_encode
from qiniu.compat import b

# refer: https://developer.qiniu.com/dora/manual/1305/processing-results-save-saveas

access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')
q = Auth(access_key, secret_key)

bucket = 'crawler-pub'
key = 'crawler/radius22.png'
host = 'http://crawler-pub.iamlj.com/'
url_with_http_param = 'http://crawler-pub.iamlj.com/1.png?roundPic/radius/50'
url_with_param = 'crawler-pub.iamlj.com/1.png?roundPic/radius/50'
encoded_entry_uri = urlsafe_base64_encode(bucket + ':' + key)
signing_str = url_with_param + '|saveas/' + encoded_entry_uri

sha1_sign = hmac.new(secret_key, b(signing_str), sha1)
encode_sign = urlsafe_base64_encode(sha1_sign.digest())
sign = access_key + ':' + encode_sign

final_url = url_with_http_param + '|saveas/' + encoded_entry_uri + '/sign/' + sign
print("触发 url:")
print(final_url)
print("新图片 url:")
print(host + key)
