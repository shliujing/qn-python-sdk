# -*- coding: utf-8 -*-
# flake8: noqa
import os

from qiniu import Auth, PersistentFop, urlsafe_base64_encode

# 对已经上传到七牛的视频发起异步转码操作
access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')
q = Auth(access_key, secret_key)

# 要转码的文件所在的空间和文件名。
bucket_name = 'test-pub'
key = 'gop/fop处理后的.mp4'

# 转码是使用的队列名称。
pipeline = '12349'

# 要进行转码的转码操作，下面是一个例子。 cWluaXUtJChjb3VudCk= 即 qiniu-$(count).mp4
fops = 'segment/mp4/segtime/10/pattern/' + urlsafe_base64_encode('qiniu-$(count).mp4')
ops = []
pfop = PersistentFop(q, bucket_name, pipeline)

ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
print(info)
assert ret['persistentId'] is not None
