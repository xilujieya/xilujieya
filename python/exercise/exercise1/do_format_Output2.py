# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 0:26
# @Author  : pat
# @FileName: do_format_Output2.py
# @Software: PyCharm

name = input("name:")
age = input("age:")
skill = input("skill:")
salary = input("salary:")

info1 = '''
 --- info of %s ---
 Name:%s
 Age:%s
 Skill:%s
 Salary:%s
''' % (name, name, age, skill, salary)

print(info1)