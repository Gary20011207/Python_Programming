# -*- coding: utf-8 -*-
# 給定任意上底、下底、高，計算梯形面積

def Trapezoid_Area(Top, Bottom, Height):
    return (Top + Bottom) * Height / 2

print(Trapezoid_Area(5, 10, 6))