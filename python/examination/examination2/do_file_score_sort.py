#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 18:20
# @Author  : pat
# @FileName: do_file_score_sort.py
# @Software: PyCharm

"""从键盘循环连续输入n个同学的姓名，语文，数学，外语成绩，保存到一个txt文件中；备注：程序测试时，n请赋值为3和5分别测试；
输入要求:
1 有提示语句“请输入第一1个同学的姓名及语数外成绩：”；
2 输入：张三 82  86  75（中间用空格隔开） 回车后，提示“请继续输入第2个同学的成绩：”；
3 n个同学的成绩保存到txt文件中（注意：原始数据文件中不允许保存总分）；
4 然后按照总分从高到低输出显示（如果总分相同，则分别按照语数外单科成绩来排序）；

输出要求：
1有表头:名次  姓名  语文  英语  数学  总分;
2 表头下是一行分隔线；效果如下："""


# 提示：请采用如下的程序结构：
# #成绩数据录入并保存到文件
# def input_grade(n):
# pass
#
# #从文件读取成绩，并排序输出打印
# def grade_sort():
# pass
#
# if __name__ == '__main__':
# n=5
# input_grade(n)
# grade_sort()


# 成绩数据录入并保存到文件
def input_grade(n):
    with open('./file/do5', 'w', encoding='UTF-8') as f:
        f.write('名次 姓名 语文 英语 数学 总分\n')
        f.write('________________________________________________________\n')
        for i in range(n):
            info = input('请继续输入第{}个同学的成绩:'.format(i + 1))
            f.write('       ' + info)
            f.write('\n')
    pass


# 从文件读取成绩，并排序输出打印
def grade_sort():
    with open('./file/do5', 'r', encoding='UTF-8') as f:
        print(f.readline().strip())
        print(f.readline().strip())
        lists = []
        for i in f:
            inform = i.strip().split(' ')
            lists.append(inform)
        lists.sort(key=lambda x: x[2] + x[3] + x[1], reverse=True)
        count = 0
        for i in lists:
            count += 1
            print(str(count) + '  ' + + '  '.join(i) + '  ' + str(int(i[1]) + int(i[2]) + int(i[3])))
    pass


if __name__ == '__main__':
    n = 5
    input_grade(n)
    grade_sort()
