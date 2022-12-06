#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 23:25
# @Author  : pat
# @FileName: dog.py
# @Software: PyCharm


class Dog:
    blood = 80
    hit = 15
    did = -1
    death = False

    def hit_dog(self, people):
        people.hit -= 3
        if people.hit <= 0:
            people.hit = 1
        people.blood -= self.hit
        print(f'序号为{people.pid + 1}的人受到攻击，体力值为{people.blood}')
        if people.blood <= 0:
            print(f'序号为{people.pid + 1}的人阵亡')
            people.death = True

    def __init__(self, did):
        self.did = did