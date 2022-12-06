# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 17:13
# @Author  : pat
# @FileName: the_dict2.py
# @Software: PyCharm

from random import randint

dic1 = {x: randint(60, 100) for x in range(1, 11)}
print(dic1)

d = {
    'name': "Tom",
    'sex': "male",
    'address': "北京市昌平区回龙观",
    'age': 25
}

for k, v in d.items():
    print('{key}:{value}'.format(key=k, value=v))

res = {k: v for k, v in dic1.items() if v > 80}
print(res)
