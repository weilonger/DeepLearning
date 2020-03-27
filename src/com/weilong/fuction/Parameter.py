#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 参数 灵活度大，有正常定义必选参数、默认参数、可变参数和关键字参数
# 位置参数 x是一个位置参数，调用时必须传入且仅有一个
# x和n也都为位置参数，调用时必须按序传入参数值
def power(x):
    return x * x


def power(x, n):
    s = 1
    for i in range(n):
        s *= x
    return s


# 默认参数 设置n的默认值为2，即使不传该参数也可以正常执行
# 必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    if n < 0:
        for i in range(abs(n)):
            s /= x
    else:
        for i in range(n):
            s *= x
    return s


print(power(2, -1))


# l、i、o、0尽量避免使用，会引起视觉歧异
def add(entry=None):
    if entry is None:
        entry = []
    entry.append("End")
    return entry


print(add([1, 2, 3]))

# 可变参数


# def calculate(num):
#     sum = 0
#     for n in num:
#         sum = sum + n * n
#     return sum


def calculate(*num):
    sums = 0
    for n in num: 
        sums = sums + n * n
    return sums


# print(calculate([1, 2, 3]))
print(calculate(1, 2, 3))
nums = [1, 2, 4]
print(calculate(*nums))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, "age:", age, "others:", kw)


# 可以传入任何个数的关键字参数
person('麒麟', 23, sex='男')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('宇辉', 24, **extra)


# 命名关键字参数 *作为特殊分隔符，*后面的参数被视为命名关键字参数
def star(name, age, *, gender, breaf):
    print(name, age, gender, breaf)


star('吴亦凡', '30', gender='男', breaf='大碗宽面')


# 如果函数中已有可变参数，不需要添加特殊分隔符*
def rapper(name, sex, *args, works, city='香港'):
    print(name, sex, args, works, city)


rapper('邓紫棋', '女', '可爱', '天籁', works=['差不多姑娘', '喜欢你', '来自天堂的魔鬼'])


# 参数组合 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
args1 = (1, 2, 3, 4)
extra1 = {'d': 99, 'x': '#'}
f1(*args1, **extra1)
args2 = (1, 2, 3)
extra2 = {'d': 88, 'x': '#'}
f2(*args2, **extra2)


# 练习
# 实现可接收一个或多个数并计算乘积的函数
def product(*num):
    multi = 1
    for a in num:
        multi *= a
    print(multi)


nums = [1, 2, 3, 4]
product(*nums)
