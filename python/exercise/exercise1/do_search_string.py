# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 23:28
# @Author  : pat
# @FileName: do_search_string.py
# @Software: PyCharm

"""定义一个字符串,分别进行查找某个字符串是否包含在这个字符串里面;
进行某个字符串的替换;
打印字符串的长度;"""

print('请输入字符串')
str1 = input()
print('请输入子串')
str2 = input()

if str1.find(str2) == -1:
    print("不存在！")
else:
    print("存在！")

print('请输入要替换的字符串')
str3 = input()
str1 = str1.replace(str2, str3)
print(str1)
print(len(str1))
