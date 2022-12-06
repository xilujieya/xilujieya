#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 16:35
# @Author  : pat
# @FileName: do3_write_file.py
# @Software: PyCharm

"""从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
        Tom   admin   XXXXX
        Jack   root   XXXXX """
import base64

list2 = []
for i in range(5):
    name = input('请输入姓名：')
    user = input('请输入用户名：')
    pwd = input('请输入密码：')
    pwd = str(base64.b64encode(pwd.encode('utf8')))
    a = name + " " + user + " " + pwd + "\n"
    list2.append(a)
with open('test1.txt', 'a') as file:
    for i in list2:
        file.write(i)

