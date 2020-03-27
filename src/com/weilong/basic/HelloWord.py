#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输入与输出
name = "麒麟"
name = input('请输入你的名字：')
print('你好,', name)
print('==========================')
# 数据类型
# 整数可以无限大小
print(0xff)
# 浮点数在很大或很小时，需要按照科学计数法表示，把10用e替换
print(1.23e9)
# 字符串主要是转义字符需要注意，另外还有内部有很多换行时可以用三引号表示
print('I\'m \"weilong\"')
print('''weilong
qilin
tingfeng''')
# 布尔值可以直接用True和False表示，也可以用表达式
print(3 > 2, True and False, True or False)
# 空值用None表示
print(None)
# 常量即不能变的变量，全部用大写的变量名表示
PI = 3.1415926
print(PI)
# 除法
print(9 / 3)
# 即使整除也会输出为浮点数
print(10 // 3)
# 无论是否整除都会输出整数
print('==========================')
