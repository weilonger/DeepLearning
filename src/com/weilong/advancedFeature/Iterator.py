#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from var_dump import var_dump
from collections.abc import *

# 迭代器 生成器都是Iterator对象，list、dict、str虽然可迭代，却不是Iterator
# 可迭代输出
print('==可迭代==')
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 迭代器输出
print('==迭代器==')
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# list、dict、str 都可以通过iter()函数转换成迭代器
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
