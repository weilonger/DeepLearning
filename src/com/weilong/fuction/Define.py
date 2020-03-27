#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


# 定义函数 使用def语句，依次写出函数名，括号，括号中参数和冒号：，然后实现函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-5))
# print(my_abs('A'))
# print(abs('A'))
# 其他文件中在Call.py中进行了调用，from src.com.weilong.fuction.Define import my_abs


# 空函数 使用pass语句,可用来当占位符，也可以在条件语句中使用，类似于java中TODO
def nop():
    pass


# 参数检查
# python参数只对个数进行了校验，会跑出TypeError，若是类型错误时，检查不出来，所以需要对参数类型进行限制
def new_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# print(new_abs('A'))


# 返回多个值 其实是返回了一个Tuple元组
def move(x, y, step, angle=0):
    xx = x + step * math.cos(angle)
    yy = y - step * math.sin(angle)
    return xx, yy


x1, y1 = move(10, 5, 3, math.pi / 6)
print(x1, y1)


# 练习
# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax^2+bx+c=0 的两个解
def quadratic(a, b, c):
    if b * b - 4 * a * c >= 0:
        xx1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        xx2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return xx1, xx2
    else:
        raise IOError('不存在合法值')


try:
    x1, x2 = quadratic(4, 3, 1)
    print(x1, x2)
except IOError:
    print("不存在合法值")
