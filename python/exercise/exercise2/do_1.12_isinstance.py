# -*- coding: utf-8 -*-
# @Time    : 2022/10/25 20:02
# @Author  : pat
# @FileName: do_1.12_isinstance.py
# @Software: PyCharm

"""如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
使用内建的isinstance函数可以判断一个变量是不是字符串
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行"""

L = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L if isinstance(s, str)]

print(L2)
