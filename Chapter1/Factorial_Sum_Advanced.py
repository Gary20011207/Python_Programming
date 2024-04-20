# -*- coding: utf-8 -*-
# 給定任意正整數n，計算由1開始到n的階乘和
def factor(n):
    n_factor = 1
    for i in range(1, n + 1):
        n_factor *= i
    return n_factor

def factor_sum(n):
    n_factor_sum = 0
    for i in range(1, n + 1):
        n_factor_sum += factor(i)
    return n_factor_sum

print(factor_sum(5))