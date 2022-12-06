#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 23:25
# @Author  : pat
# @FileName: fight.py
# @Software: PyCharm

# 1 2个角色，人和狗，游戏开始后，生成2个人，3
# 条狗，人狗互相交替对战(注意, 人只能打狗, 狗也只会咬人);
# 人的打击力为10;
# 初始化血为100;
# 狗的攻击力为
# 15;
# 初始化血为80;
# 2
# 人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话, 表示死亡, 退出游戏;
# 人和狗的攻击力, 都会因为被咬, 或者被打而降低(人被咬一次, 打击力降低2;
# 狗被打一次, 攻击力降低3);
# 3
# 对战规则:
# A
# 随机决定, 谁先开始攻击;
# B
# 一方攻击完毕后, 另外一方再开始攻击;
# 攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
# C
# 每次攻击, 双方只能安排一个人, 或者一条狗进行攻击;

from dog import *
from people import *

import random

class Fight:
    p1 = People(0)
    p2 = People(1)
    d1 = Dog(0)
    d2 = Dog(1)
    d3 = Dog(2)
    p_team = [p1, p2]
    d_team = [d1, d2, d3]
    round = 0

    def d_team_live(self):
        for item in self.d_team:
            if not item.death:
                return True
        return False

    def p_team_live(self):
        for item in self.p_team:
            if not item.death:
                return True
        return False

    def fighting(self):
        self.round = random.randint(0, 1)
        while self.p_team_live() and self.d_team_live():
        #for i in range(500):
            if self.round == 0:
                people = self.p_team[random.randint(0, 1)]
                while people.death:
                    people = self.p_team[random.randint(0, 1)]
                dog = self.d_team[random.randint(0, 2)]
                while dog.death:
                    dog = self.d_team[random.randint(0, 2)]
                people.hit_dog(dog)
                self.round = 1
            else:
                people = self.p_team[random.randint(0, 1)]
                while people.death:
                    people = self.p_team[random.randint(0, 1)]
                dog = self.d_team[random.randint(0, 2)]
                while dog.death:
                    dog = self.d_team[random.randint(0, 2)]
                dog.hit_dog(people)
                self.round = 0
            # for j in self.p_team:
            #     print(j.blood)
            #     print(j.death)
        print('game over')
        if self.p_team_live():
            print('人类方获胜')
        else:
            print('狗阵营获胜')


game = Fight()
game.fighting()