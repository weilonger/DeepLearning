#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections.abc import Iterable
from var_dump import var_dump

# 迭代 循环遍历string、dict、list或tuple
scores = {'麒麟': 95, '廷锋': 96, '义林': 97}
for score in scores:
    print(score, scores.get(score))

string = 'welcome to python'
for ch in string:
    print(ch, end="")
print('\n', end="")

# 判断某类型变量是否可迭代
print(isinstance(string, Iterable))

# enumerate函数把list变成 `索引-元素`
for key, value in enumerate(scores):
    print(key, value)

# 同时引用两个变量
for x, y in [(1, 1), (3, 5), (5, 9)]:
    print(x, y)


# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    x1 = None
    y1 = None
    if len(L) > 0:
        x1 = L[0]
        y1 = L[0]
        for l in L:
            if l < x1:
                x1 = l
            if l > y1:
                y1 = l
    t = (x1, y1)
    return t


nums = []
print(findMinAndMax(nums))
nums = [1, 2, 5, 7, 4, 3]
print(findMinAndMax(nums))

