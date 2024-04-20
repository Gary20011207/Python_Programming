# -*- coding: utf-8 -*-
def GCD(m, n):
    if m % n == 0:
        return n
    else:
        return GCD(n, m % n) # Euclidean Algorithm

print("84和1080的最大公因數為", GCD(84, 1080))