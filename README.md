# README

七牛 sdk 的笔记在`README_Qiniu.md`

client 文件夹是给客户测试的，包含客户信息。放本地，不上传。


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
- [x] 转码
- [x] 加水印
- [ ] ocr

后续考虑

- [ ] 直播回放生成/流的增删改查
- [ ] 人脸1比多
- [ ] kikr
- [ ] 日志的接口调试


## 上传+回调

/Users/jingliu/lj-local/code/qiniu-sdk/python-sdk-7.2.0/examples/lj/homework/upload_callback.py

![](http://i.iamlj.com/18-11-30/44797812.jpg)



## mkzip

"persistentId":"z0.5bbc0f0638b9f349c8d1f390"

![](http://i.iamlj.com/18-10-9/22005358.jpg)

## 私有 url

/Users/jingliu/lj-local/code/qiniu-sdk/python-sdk-7.2.0/examples/lj/homework/private_url.py

![](http://i.iamlj.com/18-11-30/47206653.jpg)

## OCR


![](http://i.iamlj.com/18-12-20/49999442.jpg)