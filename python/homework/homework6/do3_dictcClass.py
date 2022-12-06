#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/16 0:33
# @Author  : pat
# @FileName: do3_dictcClass.py
# @Software: PyCharm

"""定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})"""


class DictClass(object):
    dict = {}

    def __init__(self, dict={}):
        self.dict = dict

    def del_dict(self, key):
        self.dict.pop(key)

    def get_dict(self, key):
        for k, v in self.dict.items():
            if k == key:
                return v
            else:
                text = 'not found'
        return text

    def get_key(self):
        return list(self.dict)

    def update_dict(self, nd={}):
        for k, v in nd.items():
            self.dict[k] = v
        list1 = []
        for i in self.dict.values():
            list1.append(i)
        return list1


if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'d': 4, 'e': 5, 'f': 6}

    d = DictClass(dict1)
    d.del_dict('b')
    print(d.get_dict('c'))
    print(d.get_key())
    print(d.update_dict(dict2))
