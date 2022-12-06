# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 22:43
# @Author  : pat
# @FileName: do6_fibonacci.py
# @Software: PyCharm

"""前面2个元素为0，1，输出100以内的斐波那契数列"""

fibonacci = [0, 1]
i = 0
while fibonacci[i] + fibonacci[i + 1] < 100:
    fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    i = i + 1
print(fibonacci)
