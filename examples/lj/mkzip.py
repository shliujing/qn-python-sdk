import os

import qiniu
from qiniu import Auth, PersistentFop

#七牛端基本验证
access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')
bucket = os.getenv('QINIU_TEST_BUCKET')

q = Auth(access_key, secret_key)

#压缩
pipeline = "12349214"
key = 'mkzip/mkzip-4-index.txt'
fops = 'mkzip/4'
zipKey = 'crawler/test100911.zip';

saveas_key = qiniu.urlsafe_base64_encode(bucket+':'+zipKey)
fops = fops+'|saveas/'+saveas_key

pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret2, info2 = pfop.execute(key, ops, 1)
print(info2)
assert ret2['persistentId'] is not None
