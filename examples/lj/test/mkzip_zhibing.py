# encoding=utf8
import os

import qiniu
from qiniu import Auth, put_file, PersistentFop

#七牛端基本验证
access_key = os.getenv('QINIU_ACCESS_KEY')
secret_key = os.getenv('QINIU_SECRET_KEY')
q = Auth(access_key, secret_key)

#将文件加密
f = open("/Users/pasca/Desktop/list0.txt")
fw = open("/Users/pasca/Desktop/list2.txt", 'w')
fs = f.readlines()
for line in fs:
    f64 = qiniu.urlsafe_base64_encode(line)
    print(f64)
    fw.write("url\\")
    fw.writelines(f64)
    fw.write('\n')
fw.close()

#将索引文件上传到七牛云空间
bucket = 'lllllll'
key0 = 'index.txt'
token = q.upload_token(bucket, key0, 3600)
lf = '/Users/pasca/Desktop/list2.txt'
ret1, info1 = put_file(token, key0, lf)
#assert ret1['key0'] == key0
#assert ret1['hash'] == etag(lf)

#压缩
pipeline = "test1"
key = 'index.txt'
fops = 'mkzip/4'
saveas_key = qiniu.urlsafe_base64_encode('lllllll:test-mkzip.zip')
fops = fops+'|saveas/'+saveas_key

#fops = 'bucket='+bucket+'&key='+key+'&fops='+fops+'|saveas/'+saveas_key
#fops = 'bucket='+bucket+'&key='+saveas_key+'&fops='+fops
pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret2, info2 = pfop.execute(key, ops, 1)
print(info2)
assert ret2['persistentId'] is not None
