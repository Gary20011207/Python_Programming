# -*- coding: utf-8 -*-
# 假設兩點的座標為 (x1, y1) 和 (x2, y2)，則兩點距離公式如下： distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
x1, y1 = eval(input("請輸入第一個點的座標："))
x2, y2 = eval(input("請輸入第二個點的座標："))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("兩點距離為", distance)