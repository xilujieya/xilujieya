#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/16 1:09
# @Author  : pat
# @FileName: do4_student_package.py
# @Software: PyCharm

"""封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。"""


class Student(object):
    name = None
    age = None
    sex = None
    score = []

    def __init__(self, name, age, sex, *score):
        self.name = name
        self.age = age
        self.sex = sex
        for i in score:
            self.score.append(i)

    def get_sum(self):
        sum1 = 0
        for i in self.score:
            sum1 += i
        return sum1

    def get_avg(self):
        sum1 = 0
        for i in self.score:
            sum1 += i
        return sum1 / 3

    def print_data(self):
        print(self.name)
        print(self.age)
        print(self.sex)
        for i in self.score:
            print(i)


if __name__ == '__main__':
    stu = Student('qwe', 20, '男', 70, 80, 90)
    print(stu.get_sum())
    print(stu.get_avg())
    stu.print_data()
