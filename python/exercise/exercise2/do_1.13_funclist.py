# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 20:22
# @Author  : pat
# @FileName: do_1.13_funclist.py
# @Software: PyCharm

"""定义一个函数,  打印输出列表里面的元素;  然后增加列表中的元素, 然后再输出新的列表;
     主程序中,打印这个列表的地址(传参之前,传参之后);"""


def funclist(list):
    print(list)
    list.append('wq')
    print(list)


if __name__ == "__main__":
    print(id(list))
    list = ['qwe', 45, 'df']
    funclist(list)
    print(id(list))

