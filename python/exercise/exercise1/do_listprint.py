# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 23:37
# @Author  : pat
# @FileName: do_listprint.py
# @Software: PyCharm

"""定义一个列表,表示一个同学的学号,姓名,班级,3门课的分数;
stu=['101','张三','软件1801',[80,89,65]]
然后格式化打印输出一下；"""

stu = ['101', '张三', '软件1801', [80, 89, 65]]

print("他的学号是： %s" % stu[0])
print("他的姓名是： %s" % stu[1])
print("他的班级是： %s" % stu[2])
print("他的成绩是： %s" % stu[3])
