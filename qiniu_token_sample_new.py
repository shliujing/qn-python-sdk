# encoding:utf-8
import hmac
import os
import time
import base64
import urllib
import random
import struct
import hashlib
import requests
import json

def hmac_sha1(key, text):
    return hmac.new(key, text, hashlib.sha1).digest()

Access_Key = os.getenv('QINIU_ACCESS_KEY')
Secret_Key = os.getenv('QINIU_SECRET_KEY')
url='http://oayjpradp.bkt.clouddn.com/Audrey_Hepburn.jpg'

Method='POST'
Path='/v1/image/label'
Host='argus.atlab.ai'
contentType='application/json'


bodyStr='{"data": {"uri": "http://oayjpradp.bkt.clouddn.com/Audrey_Hepburn.jpg"}}'


data = Method+ " " + Path + "\nHost: " + Host + "\nContent-Type: " + contentType + "\n\n" + str(bodyStr)
sign = hmac_sha1(Secret_Key,data)
encodedSign = base64.urlsafe_b64encode(sign)
QiniuToken = "Qiniu " + Access_Key + ":" + encodedSign


host='http://'+ Host + Path
header={'Content-Type': contentType,'Authorization':QiniuToken}

print header 
r=requests.post(host,data=bodyStr,headers=header)
a=r.json()
a.update({'url': url})
print a 
			
