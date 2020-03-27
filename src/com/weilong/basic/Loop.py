#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环
name = ['qilin', 'weilong', 'yilin']
for n in name:
    print(n)

# range函数会生成0 -> n-1的列表
sums = 0
for x in range(10):
    sums += x
print(sums)

syn = 'y'
while syn == 'y':
    print('请输入名字:')
    name = input()
    if name == '麒麟' or name == 'qilin':
        print('傻子')
    elif name == '卫龙' or name == 'weilong':
        print('天才')
    else:
        print('未知')
    print('请确定是否继续y/n:')
    syn = input()

x = 0
while x < 50:
    x = int(input())
    if x < 0:
        break
    elif x % 2 == 0:
        print(x, '为偶数')
    else:
        continue
