#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

from var_dump import var_dump

# 函数式编程 允许把函数本身作为参数传入另外一个函数，还允许返回一个函数
# 函数名也是变量 对于ads()，可以理解为abs是指向一个可以计算绝对值得得函数
f = abs
print(f)
print(f(-10))


# 传入函数
# 高阶函数:变量可以指向函数，函数也可以接收变量，一个函数接收另外一个函数作为参数
def add(x, y, fx):
    return fx(x) + fx(y)


print(add(10, -5, f))


# map map()函数接收两个参数，一个函数，一个Iterable，map将传入函数一次作用到序列的每个元素，并把结果作为Iterator返回
def f1(x):
    return x * x


# list调用平方函数返回iterator
r = map(f1, [1, 2, 3, 4])
print(list(r))
# 将数字都转成str
s = map(str, [1, 2, 3, 4])
print(list(s))


# reduce把一个函数作用在一个序列上，这个函数需要接收两个参数
def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4]))


# 将各位数数组连接成一个数
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 4, 6, 7]))


def char2num(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]


# 数字字符串转换成数字
print(reduce(fn, map(char2num, '12356')))

# 整理成函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s2):
    def fn1(x, y):
        return x * 10 + y

    def char2num1(c):
        return DIGITS[c]
    return reduce(fn1, map(char2num1, s2))


# lamada优化
def str2int1(s3):
    def char2num2(c):
        return DIGITS[c]
    return reduce(lambda x, y: x * 10 + y, map(char2num2, s3))


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def pro(x, y):
        return x * y

    return reduce(pro, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(st):
    return str2int(st.split('.')[0]) + str2int(st.split('.')[1]) * (0.1 ** len(st.split('.')[1]))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
