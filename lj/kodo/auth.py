#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 该脚本平均每小时提交 4万5千多条URL
# 推荐 0.3s,方便及时停止抓取， 一天提交10万~15万 URL  PS：因为URL一旦提交到队列中，就不可修改

# python qiniu_big_fetch.py <ak>  <sk> <bucket> <zone(z0 z1)>  <file_path> <sleep_time>
