# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 20:29
# @Author  : pat
# @FileName: do_1.13_lambda.py
# @Software: PyCharm

"""初始化一个列表(1-20之间的整数) ; 然后 使用匿名函数,列表解析式, 来打印输出一个列表中的奇数"""

list1 = [i for i in range(1, 21)]
odd = lambda i: i % 2 == 1
list2 = list(filter(odd, list1))
print(list2)
