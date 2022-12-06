# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 0:25
# @Author  : pat
# @FileName: do_format_Output1.py
# @Software: PyCharm

name = input("name:")
age = input("age:")
skill = input("skill:")
salary = input("salary:")

info = '''
  --- info of ''' + name + ''' 
  name: ''' + name + '''
  age: ''' + age + '''
  skill: ''' + skill + '''
  salary: ''' + salary + '''
'''
print(info)