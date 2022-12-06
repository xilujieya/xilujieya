# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 16:59
# @Author  : pat
# @FileName: do_1.17_dict.py
# @Software: PyCharm

"""给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去"""

import pickle

stu = {'jack': [101, 19], 'peter': [102, 21], 'ann': [103, 29], 'andy': [104, 49], 'pat': [105, 30]}
output = open('data.pkl', 'wb')
pickle.dump(stu, output)
output.close()

pkl_file = open('data.pkl', 'rb+')
stu2 = pickle.load(pkl_file)
print(stu2)
