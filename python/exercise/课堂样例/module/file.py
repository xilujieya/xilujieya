# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 16:10
# @Author  : pat
# @FileName: file.py
# @Software: PyCharm

def func1():
    print("----------func1调用-----------")


def func2():
    print("----------func2调用-----------")


if __name__ == '__main__':
    print('----------main调用-----------')
else:
    print('--------入口跳出-------')
