#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/9 10:57
# @Author  : pat
# @FileName: do9_download.py
# @Software: PyCharm

"""从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）"""

import os
import requests
url = "https://img0.baidu.com/it/u=3667524470,518199532&fm=253&fmt=auto&app=138&f=JPEG/orange.jpeg"
d = 'E:\\python\\homework\\homework4\\orange\\'
path = d+url.split('/')[-1]
# print(path)
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("图片获取失败")
