# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 21:53
# @Author  : pat
# @FileName: do4_judge_leapyear.py
# @Software: PyCharm

"""判断用户输入的年份是否为闰年"""

a = int(input("请输入年份："))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(a, "是闰年")
else:
    print(a, "不是闰年")