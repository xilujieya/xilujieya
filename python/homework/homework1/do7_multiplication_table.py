# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 23:03
# @Author  : pat
# @FileName: do7_multiplication_table.py
# @Software: PyCharm

"""打印输出9*9乘法表，按照下面的格式"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}×{i}＝{i * j}', end='    ')
    print()
