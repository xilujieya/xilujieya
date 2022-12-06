# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 20:41
# @Author  : pat
# @FileName: do_1.14_variPara.py
# @Software: PyCharm

"""使用不定长参数定义2个函数（只定义一个形参）;分别实现对输入数据的封装(封装成一个列表和字典),然后打印输出"""


def tolist(*args):
    return list(args)


def todic(**args):
    return dict(args)


print(tolist(70, 60, 50))
print(todic(a=2, b=3))
