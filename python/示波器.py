# -*- coding: utf-8 -*-
# @Time    : 2022/10/27 21:41
# @Author  : pat
# @FileName: 示波器.py
# @Software: PyCharm

R1 = 1.5
R2 = 16000
sx = 0.02
sy = 0.05
L = 0.13
S = 1.24e-4
N1 = N2 = 100
C = 1e-6

list1 = []
list2 = []
x = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.5, 2, 2.5, 3, 4, 5]  # 列表内为数据
y = [0, 0.15, 0.3, 0.4, 0.7, 1, 1.6, 2.2, 2.8, 3.4, 3.9, 4]

for i in x:
    H = N1 * sx * i / (L * R1)
    list1.append(H)

for i in y:
    B = R2 * C * sy * i / (N2 * S)
    list2.append(B)
print("表1：")
for i in range(0, 12):
    print("第" + str(i + 1) + "次 H：" + str(list1[i]))
    print("\t  B：" + str(list2[i]))

print("表2：")
list3 = []
list4 = []
list5 = []
x2 = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
y1 = [1, 3.7, 3.6, 3.4, 3.1, 2.8, 2.3, 1.6, -0.3, -3, -4]
y2 = [4, 3, 2, -1.5, -2.4, -2.8, -3.2, -3.4, -3.6, -3.8, -4]

for i in x2:
    H = N1 * sx * i / (L * R1)
    list3.append(H)

for i in y1:
    B1 = R2 * C * sy * i / (N2 * S)
    list4.append(B1)
for i in y2:
    B2 = R2 * C * sy * i / (N2 * S)
    list5.append(B2)

for i in range(0, 11):
    print("第" + str(i + 1) + "次 H：" + str(list3[i]))
    print("\t  B1：" + str(list4[i]))
    print("\t  B2：" + str(list5[i]))
