#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 调用函数
from var_dump import var_dump
from src.com.weilong.fuction.Define import my_abs

print(abs(-10))
help(abs)
print(max(1, 2, 5, 4))
# 类型转换
var_dump(int('123'), float('12.34'), str(1.25), bool(1))
# 函数别名
jdz = abs
print(jdz(-10))
var_dump(my_abs(-20))

# 练习
# 用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
n = 255
var_dump(hex(n))

