#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from var_dump import var_dump
# dict(map)与set
# dict同map，使用key-value存储，有极快查找速度
name = ['卫龙', '麒麟', '邓超']
score = ['99', '96', '86']
d = {'卫龙': '99', '麒麟': '96', '邓超': '86'}
print(d['麒麟'])

jsObj = json.dumps(d)
print(jsObj)

# 新增值
d['廷锋'] = 100
print(d)
var_dump(d)
# 判断key是否存在于dict中
if '廷锋' in d:
    print(d['廷锋'], '成功匹配')
# key不存在时会返回None或者是指定值 注意：返回None的时候Python的交互环境不显示结果。
print(d.get('廷锋'))
print(d.get('志鹏', -1))
# 删除某个元素
print(d.pop('廷锋'))
var_dump(d)

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# set也是一组key的集合，但不存储value，无重复key值 重复元素被自动过滤
s = set(['京', '津', '冀', '豫', '津'])
t = {'京', '津', '冀', '豫', '津'}
print(s, t)
# 新增值
s.add('晋')
print(s)
