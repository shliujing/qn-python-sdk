# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, PersistentFop, urlsafe_base64_encode
import os

# 对已经上传到七牛的视频发起异步转码操作
access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')

q = Auth(access_key, secret_key)

# 要转码的文件所在的空间和文件名。
bucket = '28-crawler'
key = '4k.mp4'

# 转码是使用的队列名称。
pipeline = 'pl-lql'

# 要进行视频截图操作。

fops = 'vframe/jpg/offset/3/w/480/h/360'

# 可以对转码后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
saveas_key = urlsafe_base64_encode(bucket+':'+'2018/08/29/4k_py_1.jpg')
fops = fops+'|saveas/'+saveas_key

pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
if info.status_code==200:
    print(info)
assert ret['persistentId'] is not None