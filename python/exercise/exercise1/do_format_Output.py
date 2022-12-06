# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 0:27
# @Author  : pat
# @FileName: do_format_Output.py
# @Software: PyCharm

name = input("username：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")

info = '''
  --- info of {_name}
  Name：{_name}
  Age：{_age}
  Skill：{_skill}
  Salary：{_salary}
'''.format(_name=name, _age=age, _skill=skill, _salary=salary)

print(info)