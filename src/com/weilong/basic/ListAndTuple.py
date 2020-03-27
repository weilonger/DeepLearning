#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from var_dump import var_dump
# list列表
name = ['卫龙', '麒麟', '廷锋']
print(name)
# print(len(name))
print('===== 插入 =====')
name.append('义林')
name.insert(1, '陈鑫')
for n in name:
    print(n)
print('===== 删除 =====')
print('删除内容:', name.pop())
print('删除内容:', name.pop(1))
for n in name:
    print(n)
print('===== 替换 =====')
name[2] = '刘江'
for n in name:
    print(n)
print(''' ''')

# tuple元组 tuple元素定义时元素必须被确定下来
title = ('复仇者联盟', '魔童降世', '使徒行者')
print(title)
# 只有一个元素时，需要有逗号','来消除歧义
number = (1,)
print(number)

# 练习
# 用索引取出下面list的指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

L.sort()
var_dump(L)
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
