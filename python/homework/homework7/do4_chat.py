#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 16:43
# @Author  : pat
# @FileName: do4_chat.py
# @Software: PyCharm

"""多进程通讯：
  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；"""

from multiprocessing import Process, Queue
import time


def write_task(q, text):
    if not q.full():
        for i in range(5):
            message = "消息:" + text[i]
            q.put(message)
            print("写入", message)


def read_task(q):
    time.sleep(1)
    while not q.empty():
        print("读取: %s" % q.get(True, 2))


if __name__ == "__main__":
    q = Queue()
    text = []
    for i in range(5):
        text.append(input("请输入消息:"))
    pw = Process(target=write_task, args=(q, text))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
