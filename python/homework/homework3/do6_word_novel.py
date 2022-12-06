#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 1:31
# @Author  : pat
# @FileName: do6_word_novel.py
# @Software: PyCharm

"""对一篇英文小说，进行词频统计，输出前20个出现频率最高的单词；"""


def getText():
    txt1 = open("./file/hamlet.txt", "r", encoding='UTF-8-sig').read()
    txt1 = txt1.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_\'{|}~\n':
        txt1 = txt1.replace(ch, "")
    return txt1


def turn_dic(lists):
    dic = {}
    for item in lists:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic[0:20])


text = getText()
text = text.strip()
list_txt = text.split(sep=' ')
turn_dic(list_txt)
