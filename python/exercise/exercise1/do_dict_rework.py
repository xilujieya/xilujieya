# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 0:09
# @Author  : pat
# @FileName: do_dict_rework.py
# @Software: PyCharm

"""字典的元素的增加, 修改,删除; 并观察输出;"""

dic1 = {'学号': 1001, '姓名': '张三', '班级': '软件1801', '年龄': 21}

dic1['年龄'] = 22
print(dic1)
dic1['成绩'] = 99
print(dic1)
del dic1['学号']
print(dic1)
