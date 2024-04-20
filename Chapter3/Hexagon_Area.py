# -*- coding: utf-8 -*-
# 假設正多邊形的邊數為n，邊長為s，正多邊形的面積為area = (n * s^2) / 4 * tan(pi / n)
import math

s = eval(input("請輸入正六邊形的邊長："))
area =  (6 * (s ** 2)) / (4 * math.tan(math.pi / 6))
print("邊長", s, "的正六邊形面積為", area)