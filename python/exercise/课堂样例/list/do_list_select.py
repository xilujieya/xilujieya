# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 16:55
# @Author  : pat
# @FileName: do_list_select.py
# @Software: PyCharm

import random

data = []
for i in range(10):
    data.append(random.randint(-100, 100))
res = []

for x in data:
    if x > 0:
        res.append(x)
print(res)
