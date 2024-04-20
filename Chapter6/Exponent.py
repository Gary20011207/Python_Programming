# -*- coding: utf-8 -*-
# e = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / 4! + ... + 1 / n!
import math

def e(n):
    return sum([1 / math.factorial(i) for i in range(n)]) # 0! = 1

print(e(5))
print(e(10))
print(e(100))
print(e(1000))