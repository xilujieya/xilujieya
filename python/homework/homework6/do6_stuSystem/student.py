#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/16 1:22
# @Author  : pat
# @FileName: student.py
# @Software: PyCharm

class student(object):
    clazz = None
    num = None
    name = None
    python_score = 0

    def __init__(self, clazz, num, name, python_score):
        self.clazz = clazz
        self.num = num
        self.name = name
        self.python_score = python_score

    def __str__(self):
        return "%s %s %s %s" % (self.num, self.clazz, self.name, self.python_score)

    @property
    def no(self):
        return self.num

    @property
    def score(self):
        return self.python_score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('成绩必须是整数')
        elif value < 0 or value > 100:
            raise ValueError("成绩应在0到100之间")
        self._score = value

    def writeToFile(self, f):
        f.write(self.__str__())
        f.write('\n')
