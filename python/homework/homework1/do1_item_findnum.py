# -*- coding: utf-8 -*-
# @Time    : 2022/10/18 21:48
# @Author  : pat
# @FileName: do1_item_findnum.py
# @Software: PyCharm

"""元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数"""

list1 = []
for i in range(51):
    if i % 2 != 0:
        list1.append(i)
print("奇数：")
print(list1)

list2 = []
for i in range(51):
    if i % 2 == 0:
        list2.append(i)
print("偶数：")
print(list2)

list3 = []
for i in range(51):
    k = 0
    for j in range(1, i + 1):
        if i % j == 0:
            k += 1
    if k == 2:
        list3.append(i)
print("质数：")
print(list3)

list4 = []
for i in range(51):
    if i % 2 == 0 and i % 3 == 0:
        list4.append(i)
print("能同时被2和3整除的数：")
print(list4)
