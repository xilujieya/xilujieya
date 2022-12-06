#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 15:27
# @Author  : pat
# @FileName: do2_judge_date.py
# @Software: PyCharm

"""定义一个函数，判断一个输入的日期，是当年的第几周，周几？
将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）"""
import datetime


def get_Date(start_date, search_date):
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    search = datetime.datetime.strptime(search_date, '%Y-%m-%d')
    week = int(search.strftime('%W')) - int(start.strftime('%W')) +1
    day = (int(search.strftime('%j')) - int(start.strftime('%j'))) % 7
    # print(search.strftime('%j'), start.strftime('%j'))
    # print(datetime.datetime(2021, 2, 17).isocalendar()[2])
    day = (day + datetime.datetime(2021, 2, 17).isocalendar()[2]) % 7
    return week, day


start_Date = '2021-2-17'
search_Date = input('输入年月日：')
n, m = get_Date(start_Date, search_Date)
print(f'第{n}周,第{m}天')

