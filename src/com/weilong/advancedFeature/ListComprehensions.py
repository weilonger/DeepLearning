#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from var_dump import var_dump

# 列表生成式，python内置的创建list的生成式
nums = list(range(1, 11))
print(nums)

# 生成1-10的平方值
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 也可以直接调用循环值,还可以跟上筛选条件
LL = [x * x for x in range(1, 11) if x % 2 == 0]
print(LL)

# 还可以组成全排列
M = [m + n for m in 'ABC' for n in 'XYZ']
print(M)

# 输出当前目录下所有文件和目录名
MM = [d for d in os.listdir(os.getcwd())]
print(MM)

# for同时使用两个甚至多个变量
d = {'x': 'X', 'y': 'Y', 'z': 'Z'}
for k, v in d.items():
    print(k, '=', v)

# 使用两个变量生成list
N = [k + '=' + v for k, v in d.items()]
print(N)

# 还可以调用字符串函数
NN = ['Hello', 'World', 'Welcome', 'Congratulate']
P = [n.lower() for n in NN]
print(P)

# 练习
# 使用内建的isinstance函数可以判断一个变量是不是字符串，修改列表生成式，通过添加if语句保证列表生成式能正确地执行
Q = ['Hello', 'World', 18, 'Apple', None]
# QQ = [q.lower() for q in Q] 会报错，只能将字符串的大写字母小写
QQ = [q.lower() for q in Q if isinstance(q, str)]
print(QQ)
