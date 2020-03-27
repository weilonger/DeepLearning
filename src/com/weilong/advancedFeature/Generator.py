#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from var_dump import var_dump

# 生成器 一边循环一边计算
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print(g)
print(next(g), next(g), next(g))
# 建立生成器后一般都不使用next()调用，而是通过for循环来迭代 当next()调用超出范围时会报StopIteration错误
for n in g:
    print(n)


# 斐波拉切数列，除第一个和第二个数外，任何一个数由前面两个数相加得到
def fib(m):
    t, a, b = 0, 0, 1
    print('========')
    while t < m:
        print(b)
        a, b = b, a + b
        t = t + 1
    return 'done'


fib(6)


# 若函数定义中包含yield关键字，该函数是一个生成器
def fib1(m):
    t, a, b = 0, 0, 1
    while t < m:
        yield b
        a, b = b, a + b
        t = t + 1
        return 'done'


f = fib1(5)
# print(f, next(f), next(f))


# 生成器和函数执行流程不一样，函数式顺序执行，遇到return语句或者最后一行函数语句就返回；
# 生成器每次调用next()执行，遇到yield返回，在此执行从上次返回的yield语句处执行
h = fib1(6)
print('========')
while True:
    try:
        x = next(h)
        print('x =', x)
    except StopIteration as e:
        print('exception:', e.value)
        break


# 练习
# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list
def triangles(i=0):
    Last = [1]
    # print(Last)
    yield Last
    while True:
        i = i - 1
        L = [1]
        for x in range(1, len(Last)):
            L.append(Last[x - 1]+Last[x])
        L.append(1)
        Last = L[:]
        print(Last)
        yield L
        if i == 0:
            break


temp = triangles(10)
print(list(temp))
