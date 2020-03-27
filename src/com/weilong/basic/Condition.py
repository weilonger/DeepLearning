#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断
print('请输入名字:')
name = '麒麟'
# name = input()
if name == '麒麟' or name == 'qilin':
    print('傻子')
elif name == '卫龙' or name == 'weilong':
    print('天才')
else:
    print('未知')

s = input()
# input函数返回值是str类型
year = int(s)
if year > 2000:
    print('00后')
else:
    print('00前')
