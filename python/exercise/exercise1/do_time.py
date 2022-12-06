# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 18:42
# @Author  : pat
# @FileName: do_time.py
# @Software: PyCharm

"""导入时间模块，显示当前的时间；显示当前的日期"""

import time

print(time.asctime(time.localtime(time.time())))
