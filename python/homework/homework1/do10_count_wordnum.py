# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 23:43
# @Author  : pat
# @FileName: do10_count_wordnum.py
# @Software: PyCharm

"""给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
   提示：可以用字典来统计：key 是单词，value 是单词出现次数；
    先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1；
    如果这个单词没出现过，就直接 插入这个单词及value 为 1 到 字典中"""

s = "Don't ever let someone tell you that you can't do something. Not even me. You get a dream, go get it."
s_data1 = s.lower()
s_data2 = s_data1.replace(",", " ").replace(".", " ")

wordlist = s_data2.split()

wordDic = {}
for i in wordlist:
    if i in wordDic:
        wordDic[i] += 1
    else:
        wordDic[i] = 1
re_list = sorted(wordDic.items(), key=lambda x: x[1], reverse=True)
print(re_list)
