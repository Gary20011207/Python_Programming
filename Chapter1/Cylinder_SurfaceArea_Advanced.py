# -*- coding: utf-8 -*-
# 給定任意半徑以及高度，計算圓柱表面積
import math
def Cylinder_SurfaceArea(r, h):
    return math.pi * r * r * 2 + 2 * math.pi * r * h

print(Cylinder_SurfaceArea(10, 5))