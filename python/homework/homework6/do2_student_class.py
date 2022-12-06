#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 17:56
# @Author  : pat
# @FileName: do2_student_class.py
# @Software: PyCharm

"""定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:"""


class Student(object):
    name = None
    age = None
    score = []

    def __init__(self, name, age, *score):
        self.name = name
        self.age = age
        for i in score:
            self.score.append(i)

    def get_name(self):
        return self.name

    def get_age(self):
        return int(self.age)

    def get_course(self):
        course = 0
        for i in self.score:
            course = max(int(i), course)
        return course


if __name__ == '__main__':
    stu = Student('zhangsan', 20, 90, 90, 81)
    print(stu.get_name())
    print(stu.get_age())
    print(stu.get_course())

