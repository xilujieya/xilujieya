# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 17:05
# @Author  : pat
# @FileName: the_dic1.py
# @Software: PyCharm

d = {
    'name': "Tom",
    'sex': "male",
    'address': "北京市昌平区回龙观",
    'age': 25
}

print("年龄是：" + d['name'])

d['age'] = 26
print(d)

print(d.keys())
print(d.values())
