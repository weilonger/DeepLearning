#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(10))


# 尾递归 当数值超出一定值时会出现栈溢出的现象 python未做尾递归优化，还是会导致栈溢出
def fact_tail(num, res):
    if num == 1:
        return res
    return fact_tail(num - 1, num * res)


# 练习
# 汉诺塔 编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def move(n, a, b, c):
    if n == 1:
        echo(a, c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


i = 0


def echo(a, c):
    global i
    i = i + 1
    print('第', i, '步', a, '-->', c)


move(3, 'a', 'b', 'c')
