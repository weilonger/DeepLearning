#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from var_dump import var_dump

# 排序算法 内置sorted()函数
L = [36, 24, 48, 78, 2, 90, 8]
print(sorted(L))

# sorted()也是高阶函数，允许接收一个key函数来实现自定义排序
L1 = [-1, 5, 25, -87, -56, 34]
# noinspection PyTypeChecker
print(sorted(L1), sorted(L1, key=abs))

# 反向排序时，可以传入第三个参数，reverse=True
print(sorted(L1, reverse=True))


# 练习
# 假设我们用一组tuple表示学生名字和成绩：用sorted()对列表分别按名字排序
L2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


# 按照成绩从高到低
def by_score(t):
    return t[1]


print(sorted(L2, key=by_name), sorted(L2, key=by_score, reverse=True), sep='\n')
