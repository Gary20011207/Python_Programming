# -*- coding: utf-8 -*-
# 給定任意半徑以及高度，計算圓柱體積
import math
def Cylinder_Volume(r, h):
    return math.pi * r * r * h

print(Cylinder_Volume(10, 5))