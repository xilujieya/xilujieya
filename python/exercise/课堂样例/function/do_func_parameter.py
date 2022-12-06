# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 17:20
# @Author  : pat
# @FileName: do_func_parameter.py
# @Software: PyCharm

# # 可写函数说明
# def printinfo(arg1, *vartuple):  # *可变参数
#     print("输出：")
#     print(arg1)
#     print(vartuple)
#     for i in vartuple:
#         print(i)
#
# printinfo(70, 60, 20, 80)


def printinfo(arg1, **vartuple):
    print("输出：")
    print(arg1)
    print(vartuple)


printinfo(1, a=2, b=3)
