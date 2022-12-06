#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 17:26
# @Author  : pat
# @FileName: do1_dog_class.py
# @Software: PyCharm

"""定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;"""


class Dog(object):
    data = [{'color': 'blue', 'num': 3, 'price': 15},
            {'color': 'black', 'num': 3, 'price': 35},
            {'color': 'yellow', 'num': 1, 'price': 25}]

    def sell(self, color, num):
        for i in self.data:
            if i['color'] == color:
                if i['num']-num >= 0:
                    i['num'] -= num
                else:
                    print('数量不足')


if __name__ == '__main__':
    d = Dog()
    d.sell('blue', 2)
    d.sell('yellow', 1)
    for i in d.data:
        print(i['color'], " ", i['num'])
