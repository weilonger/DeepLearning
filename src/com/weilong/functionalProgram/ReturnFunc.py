#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from var_dump import var_dump


# 返回函数 函数作为返回值
def sums(*args):
    sum1 = 0
    for n in args:
        sum1 = sum1 + n
    return sum1


def lazy_sum(*args):
    def sum2():
        al = 0
        for n in args:
            al = al + n
        return al
    return sum2


temp = lazy_sum(1, 2, 3, 4)
print(temp())
# 当调用lazy_sum函数时，每次调用都会返回一个新的函数
temp1 = lazy_sum(1, 2, 3, 4)
print(temp == temp1)


# 闭包 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用， 闭包使用简单，实现不容易
def count():
    L = []
    for i in range(1, 4):
        def fn():
            return i * i
        L.append(fn)
    return L


f1, f2, f3 = count()
print(f1(), f2(), f3())
# !!! 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量


# 引用循环变量
def count1():
    def fn(j):
        def g():
            return j*j
        return g
    LL = []
    for i in range(1, 4):
        LL.append(fn(i))
    return LL


f1, f2, f3 = count1()
print(f1(), f2(), f3())


# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    i = 0

    def counter():
        nonlocal i
        i += 1
        return i
    return counter


# 使用list实现
def createCounter():
    L = [0]

    def counter():
        L[0] += 1
        return L[0]
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())