# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 0:13
# @Author  : pat
# @FileName: do_set.py
# @Software: PyCharm

"""定义一个集合类型的变量(用2种方法初始化),然后进行相应的 元素的操作"""

s1 = set([1, 5, 6, 8])
s2 = {2, 6, 8, 9}
print(s1)
print(s2)

s1.add(9)
s1.remove(1)
print(s1)

print(len(s1))
print(9 in s1)