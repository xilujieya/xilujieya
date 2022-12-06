# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 17:08
# @Author  : pat
# @FileName: do_json.py
# @Software: PyCharm

import json

dict1 = {"name": "zhangsan", "gender":"男"}
print(type(dict1))

data_str = json.dumps(dict1)
print(type(data_str))

data_dict = json.loads(data_str)

print(type(data_dict))