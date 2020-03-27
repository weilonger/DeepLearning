#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from var_dump import var_dump


# filter 过滤序列 接收一个函数和一个序列，传入的函数主要做判断，返回True或False
# 过滤偶数
def is_odd(nu):
    return nu % 2 == 1


LL = [x * x + y for x in range(1, 10) for y in range(5, 10)]
print(list(filter(is_odd, LL)))


# 去除空字符串
def is_empty(ss):
    return ss and ss.strip()


print(is_empty(''), bool(is_empty('')))
L1 = ['A', '', None, 'C', ' ', 'abc']
print(list(filter(is_empty, L1)))


# filter求素数
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017404530360000 讲解地址
# 构造从3开始的奇数 2是第一个质数，2的倍数均为非质数
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选出剩余数列中不是最开始值的倍数的所有数
def is_filter(div):
    return lambda x: x % div > 0


# 获取质数
def prime(t=1000):
    num = 2
    i = 1
    yield num
    # 初始序列
    it = odd_iter()
    while True:
        if t - i == 0:
            break
        i = i + 1
        # 返回序列的第一个数
        num = next(it)
        yield num
        it = filter(is_filter(num), it)


print(list(prime(20)))


# 练习
# 回数是指从左向右读和从右向左读都是一样的数,利用filter()筛选出回数
def is_palindrome(n):
    str_n = str(n)
    str_n1 = str_n[::-1]
    return str_n == str_n1


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                  101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
