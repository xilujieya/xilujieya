#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 1:17
# @Author  : pat
# @FileName: do2_access_urllib.py
# @Software: PyCharm

""" 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
提示 ：使用requests模块"""

import threading
import requests


def exception(url):
    try:
        r = requests.get(url=url, allow_redirects=False)
        if r.status_code == 200:
            if r.apparent_encoding == 'utf-8':
                r.encoding = 'utf-8'
            print(url + '\t')
        else:
            print(url + '\t访问页面出错')
            with open('访问页面出错.txt', 'a') as f:
                f.writelines(url + '\n')
    except requests.exceptions.ConnectionError:
        print(url + '\t未知的服务器')
        with open('未知的服务器.txt', 'a') as f:
            f.writelines(url + '\n')
    except requests.exceptions.ConnectTimeout:
        print(url + '\t连接、读取超时')
        with open('连接读取超时.txt', 'a') as f:
            f.writelines(url + '\n')


def urls(*lines):
    for line in lines:
        if line == '\n':
            pass
        else:
            line = line.replace(' ', '').replace('\t', '').replace('\n', '')
            if line[0:4] == 'http':
                exception(line)
            else:
                url_h = 'https://' + line
                exception(url_h)
                url_hs = 'https://' + line
                exception(url_hs)
    file.close()


if __name__ == '__main__':
    file = open('url_data.txt')
    lines = file.readlines()
    print('开始检查：')
    file = open('url_data.txt')
    lines = file.readlines()
    for i in range(200):
        t = threading.Thread(target=urls, args=lines[i * 10:(i + 1) * 10])
        t.start()
