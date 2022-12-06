# -*- coding: utf-8 -*-
# @Time    : 2022/10/24 16:10
# @Author  : pat
# @FileName: 密立根.py
# @Software: PyCharm
import math

list = []
e0 = 1.60217662e-19
sum = 0
for i in range(1, 6):
    U = float(input('请输入第' + str(i) + '次平衡电压'))
    T = float(input('请输入第' + str(i) + '次运动时间'))
    e = (199.828e-3 / U) * math.sqrt((2.928e-8 / T) ** 3) * math.sqrt(
        (1 / (1 + 0.0219467 * math.sqrt(T))) ** 3) * 0.0102
    print('测量油滴的电荷量：' + str(e))
    n = round(e / e0)  # 四舍五入保留整数
    print('元电荷整数倍' + str(n))
    ei = e / int(n)
    print('测量元电荷：' + str(ei))
    list.append(ei)

b = len(list)
for i in range(b):
    sum = sum + list[i]
ei0 = sum / b
print("平均所测元电荷值" + str(ei0))

Er = (abs(float((e0 - ei0) / e0))) * 100
print('相对误差' + str(Er) + '%')
