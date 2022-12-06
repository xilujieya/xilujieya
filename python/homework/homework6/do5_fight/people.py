#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 23:25
# @Author  : pat
# @FileName: people.py
# @Software: PyCharm


class People:
    blood = 100
    hit = 10
    pid = -1
    death = False

    def hit_dog(self, dog):
        dog.hit -= 3
        if dog.hit <= 0:
            dog.hit = 1
        dog.blood -= self.hit
        print(f'序号为{dog.did + 1}的狗受到攻击，体力值为{dog.blood}')
        if dog.blood <= 0:
            print(f'序号为{dog.did + 1}的狗阵亡')
            dog.death = True

    def __init__(self, pid):
        self.pid = pid