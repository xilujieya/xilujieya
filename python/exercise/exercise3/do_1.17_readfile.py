# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 16:06
# @Author  : pat
# @FileName: do_1.17_readfile.py
# @Software: PyCharm


"""读取文件里面的内容(包含中文), 进行打印输出显示;
 注意:  请设置文件的不同编码格式进行观察;  另外,文件内容中包含中文字符;"""

try:
    with open(r'E:\python\exercise\exercise3\file\b_file\a.txt', encoding="UTF-8") as file1:
        print(file1.read())
except UnicodeDecodeError:
    print("无法以UTF-8编码打开中文")

with open(r'E:\python\exercise\exercise3\file\b_file\a.txt', encoding="gbk") as file2:
    print(file2.read())
