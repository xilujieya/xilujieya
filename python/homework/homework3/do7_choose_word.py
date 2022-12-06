#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 1:32
# @Author  : pat
# @FileName: do7_choose_word.py
# @Software: PyCharm

"""对一篇中文文献, ;利用jieba库,进行词频统计分析找出文章的关键词(取词频最高的前10个词语,作为文章的关键字);"""
import jieba as jieba

jieba.setLogLevel(jieba.logging.INFO)

dic = {}

with open('./file/chinese_paper', 'r', encoding='UTF-8') as f:
    txt = f.read()

words = jieba.lcut(txt)

for word in words:
    if len(word) <= 1:
        continue
    else:
        dic[word] = dic.get(word, 0) + 1

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for i in range(10):
    print('{0:<5}{1:>5}'.format(dic[i][0], dic[i][1]))