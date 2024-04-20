# -*- coding: utf-8 -*-
# 給定以Base為底，x , y的值，且給定a, b, c的值，計算10^(a * log(Base)x + b * log(Base)y + c)
import math

def Log_Advanced(Base, x, y, a, b, c):
    return pow(10, a * math.log(x, Base) + b * math.log(y , Base) + c)

print(Log_Advanced(10, 2, 3, 2, 3, 1))