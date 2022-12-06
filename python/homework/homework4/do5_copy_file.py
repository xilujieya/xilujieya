#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 17:08
# @Author  : pat
# @FileName: do5_copy_file.py
# @Software: PyCharm

"""通过Python来模拟实现一个txt文件的拷贝过程"""

import os
import shutil
import sys

source = 'do1_deque.py'
target = 'copy'

assert not os.path.isabs(source)
target = os.path.join(target, os.path.dirname(source))

os.makedirs(target)

try:
    shutil.copy(source, target)
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())
