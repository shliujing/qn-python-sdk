#!/usr/bin/python
# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag, urlsafe_base64_encode

access_key = 'VYw7rh_P_P6g6IH_v0zw1Upry5muffStXIly8AsS'
secret_key = 'ctSGEg8UXy_MNpjMbcHf66zISEXX69cRogZVurIk'

# 初始化Auth状态å
q = Auth(access_key, secret_key)

# 你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'crawler-pub'
key = 'mov/crawler.mov'

# 指定转码使用的队列名称
pipeline = ''

# 设置转码参数（以视频转码为例）
fops = 'avthumb/mp4/ab/128k/ar/22050/acodec/libfaac/r/30/vb/300k/vcodec/libx264/s/320x240/autoscale/1/stripmeta/0'

# 通过添加'|saveas'参数，指定处理后的文件保存的bucket和key，不指定默认保存在当前空间，bucket_saved为目标bucket，bucket_saved为目标key
saveas_key = urlsafe_base64_encode('crawler-pub:crawler-after.mov')

fops = fops+'|saveas/'+saveas_key

# 在上传策略中指定fobs和pipeline
policy = {
  'persistentOps': fops,
  'persistentPipeline': pipeline
 }

token = q.upload_token(bucket_name, key, 3600, policy)

localfile = './python_video.flv'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
