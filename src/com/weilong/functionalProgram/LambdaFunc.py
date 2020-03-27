#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from var_dump import var_dump


# 匿名函数 map会根据提供的函数对指定序列做映射
# 匿名函数不用return值，返回值就是表达式的结果，另外匿名函数没有名称，无需担心名称冲突
L = list(map(lambda x: x * x, range(1, 10)))
print(L)


# 以上匿名函数lambda x: x * x
def f(x):
    return x * x


