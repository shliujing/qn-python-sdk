# README

七牛 sdk 的笔记在`README_Qiniu.md`

## 已调试 demo

- cdn_log.py
 
获取指定域名指定时间内的日志链接

- mkzip.py

压缩文件

- mkzip_zhibing.py

志兵版本，貌似有点问题。忽略。

- pfop_vframe.py

对已经上传到七牛的视频发起异步转码操作

- private_url.py

生成私有 url

- upload.py

简单上传

## 计划调试 demo

主要调试几个 demo

- [x] 上传，done
- [x] 私有url
- [x] bucket列表
- [x] 刷新 cdn
- [ ] 异步fetch
- [ ] 转码
- [ ] 加水印
- [ ] ocr

后续考虑

- [ ] 直播回放生成/流的增删改查
- [ ] 人脸1比多
- [ ] kikr
- [ ] 日志的接口调试


## 上传+回调

/Users/jingliu/lj-local/code/qiniu-sdk/python-sdk-7.2.0/examples/lj/homework/upload_callback.py

![](http://i.iamlj.com/18-11-30/44797812.jpg)
