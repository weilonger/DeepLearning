#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from var_dump import var_dump

# 切片 切分str、list或tuple,类似于java中subString
surname = ('赵', '钱', '孙', '李', '周', '吴', '郑', '王')
print(surname[:5], surname[-5:], surname[1:6])
# 前6个每两个取一个
print(surname[:6:2])
print(surname[::3])
# 倒叙输出
print(surname[::-1])


# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格 str.strip()函数
def trim(s):
    # return str.strip(s)
    while s[0:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


print(trim('  sss  '))
