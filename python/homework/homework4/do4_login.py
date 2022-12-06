#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 16:58
# @Author  : pat
# @FileName: do4_login.py
# @Software: PyCharm

"""(继续上面的练习) 模拟用户登录:
     5个同学的姓名,账号和密码(加密后的),保存在一个文件上;
     系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);"""
import base64

name = input('请输入姓名:')
with open('test1.txt', 'r') as f:
    for i in f.readlines():
        data = i.split(" ")
        if name == data[0]:
            user = input('请输入用户名:')
            if user == data[1]:
                pwd = input('请输入密码：')
                k = data[2]
                k = k[2:-2]
                print(k)
                k = str(base64.b64decode(k))
                k = k[2:-1]

                if pwd == k:
                    print('登录成功')
                    break
                else:
                    print('密码错误')
            else:
                print('用户名错误')
        else:
            print('姓名没找到')