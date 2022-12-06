#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 1:33
# @Author  : pat
# @FileName: do8_likely_degree.py
# @Software: PyCharm

"""8 在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;
  并分别输出统计结果到另外的文件存放;
  比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);"""


def turn_dic(txt, dic):
    txt = txt.split()
    for item in txt:
        if len(item) <= 1:
            continue
        else:
            dic[item] = dic.get(item, 0) + 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return dic


def getText(txt):
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_\'{|}~\n':
        txt = txt.replace(ch, "")
    return txt


with open('./file/English1.txt', 'r') as f1:
    txt1 = f1.read()
    txt1 = getText(txt1)
with open('./file/English2.txt', 'r') as f2:
    txt2 = f2.read()
    txt2 = getText(txt2)
dic1 = {}
dic2 = {}
dic1 = turn_dic(txt1, dic1)
dic2 = turn_dic(txt2, dic2)
with open('./file/English_paper_key.txt', 'w', encoding='UTF-8') as f:
    f.write('论文1关键词：\n')
    f.write(str(dic1) + '\n')
    f.write('论文2关键词：\n')
    f.write(str(dic2) + '\n')
gather1 = set(dict(dic1[0:10]).keys())
gather2 = set(dict(dic2[0:10]).keys())
print('相似度：{}%'.format(len(gather1 & gather2) * 10))
