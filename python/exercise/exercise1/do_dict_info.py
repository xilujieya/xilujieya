# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 23:59
# @Author  : pat
# @FileName: do_dict_info.py
# @Software: PyCharm

"""定义一个字典,存放某个同学的信息(学号,姓名,班级,年龄); 再定义另外一个字典,存放5个同学的学号,姓名信息;
通过键来访问相应的数据; 或者整体输出"""

dic1 = {'学号': 1001, '姓名': '张三', '班级': '软件1801', '年龄': 21}
dic2 = {1: {'学号': 1001, '姓名': '张三'}, 2: {'学号': 1002, '姓名': '李四'}, 3: {'学号': 1003, '姓名': '王五'},
        4: {'学号': 1004, '姓名': '赵六'}}


print(dic1)
print(dic2)
print(dic1.values())
for k, v in dic1.items():
    print('{key}:{value}'.format(key=k, value=v))
