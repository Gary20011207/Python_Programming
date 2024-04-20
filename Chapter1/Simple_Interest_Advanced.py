# -*- coding: utf-8 -*-
# 給定任意金錢數目，年利率，年份，計算單利本利和
def Simple_Interest(Principal,APR,Year):
    return Principal * (1 + (APR * 0.01) * Year)

print(Simple_Interest(1000000, 6, 3))