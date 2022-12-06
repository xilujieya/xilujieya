#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/12 22:25
# @Author  : pat
# @FileName: do3_approve.py
# @Software: PyCharm

"""编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）"""

flag = False


def wrapper(func):
    def inner(*args, **kwargs):
        global flag
        if flag:
            res = func(*args, **kwargs)
            return res
        else:
            usr = input('请输入用户名:')
            password = input('请输入密码：')
            if usr == '123' and password == '123':
                flag = True
                res = func(*args, **kwargs)
                return res
            else:
                print('函数调用权限不足')
                print('对于函数{0}的访问被拒绝'.format(func.__name__))
    return inner


@wrapper
def print_log():
    print("admin is log here")


@wrapper
def add_user(name):
    print("user added:{0}".format(name))


print_log()
add_user(name='pat')
add_user(name='jack')
