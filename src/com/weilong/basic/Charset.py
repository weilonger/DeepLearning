#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符串和编码
print(ord('A'), ord('中'))
print(chr(66), chr(25991))
# 编码
string = 'ABC'
print(string.encode('ascii'))
string = '中文'
# 含有中文字符的字符串不能使用ascii编码，可以使用utf-8编码
print(string.encode('utf-8'))
# print(string.encode('ascii'))
# 解码
temp = b'ABC'
print(temp.decode('ascii'))
temp = b'\xe4\xb8\xad\xe6\x96\x87'
print(temp.decode('utf-8', errors='ignore'))

# 长度获取
print(len('ABC'), len('中文'), len(b'ABC'))

# 格式化 %s字符串 %d整数替换 %?占位符
print('%s今年%d岁' % ('麒麟', 23))
string = '麒麟价值{0:.1f},卖了{1:.2f}'
print(string.format(50, 60))

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('小明成绩提升了%.1f%%' % r)
