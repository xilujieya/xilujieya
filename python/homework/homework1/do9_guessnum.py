# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 23:37
# @Author  : pat
# @FileName: do9_guessnum.py
# @Software: PyCharm

"""设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败"""

import random

n = int(input('请输入猜测的次数'))
x = random.randint(1, 100)
for i in range(n):
    y = int(input('请输入你猜测的数'))
    if y == x:
        print("正确")
        break
    elif y > x:
        print("输入的值大了")
    elif x > y:
        print("输入的值小了")
    if i == n-1:
        print("失败")
