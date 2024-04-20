# -*- coding: utf-8 -*-
# 給定任意金錢數目，年利率，年份，計算複利本利和
def Compound_Interest(Principal,APR,Year):
    return Principal * ((1 + (APR * 0.01)) ** Year)

print(Compound_Interest(1000000, 6, 3))