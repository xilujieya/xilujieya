#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 17:37
# @Author  : pat
# @FileName: do_dict_input.py
# @Software: PyCharm

"""字典列表初始化--2.5'
有一个字典数组，存放了一个小组N个同学的信息；参考结构如下：
[
{
"name":"marry",
"city":"北京",
"age":"20"
},
{
"name":"tom",
"city":"上海",
"age":"20"
}
......
]
A  请从键盘输入数据，初始化这N个同学的信息；
B  按照年龄从大到小的顺序，输出这N个同学的信息；"""

stu = []
name = 'name'
city = 'city'
age = 'age'
for i in range(10):
    info = {}
    info.update({name: input('请输入名字')})
    info.update({city: input('请输入城市')})
    info.update({age: input('请输入年龄')})
    stu.append(info)

stu.sort(key=lambda x: x['age'], reverse=True)
print(stu)

