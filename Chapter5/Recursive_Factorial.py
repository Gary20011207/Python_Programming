# -*- coding: utf-8 -*-
def F(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * F(n - 1)
    else:
        return -1

print("0! =", F(0))
print("5! =", F(5))