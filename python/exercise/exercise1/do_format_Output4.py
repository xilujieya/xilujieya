# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 0:28
# @Author  : pat
# @FileName: do_format_Output4.py
# @Software: PyCharm

name = input("name：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")

info = '''
  --- info of {0}---
  Name：{0}
  Age：{1}
  Skill：{2}
  Salary：{3}
'''.format(name, age, skill, salary)

print(info)