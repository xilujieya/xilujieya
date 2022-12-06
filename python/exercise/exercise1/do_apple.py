# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 0:21
# @Author  : pat
# @FileName: do_apple.py
# @Software: PyCharm

"""提示输入需要购买的苹果的重量(斤),然后提示输入每斤的价格,请计算应支付的总价,并打印提示输出"""

print("输入需要购买的苹果的重量(斤)")
a = int(input())
print("输入每斤的价格")
b = int(input())
c = a * b
print('应支付的总价:'+str(c))
