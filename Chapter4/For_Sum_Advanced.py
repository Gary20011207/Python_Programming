# -*- coding: utf-8 -*-
# 計算費波那契數Fib(0) ~ Fib(10)

def Fibonacci(Num):
    if Num == 0:
        return 0
    elif Num == 1:
        return 1
    else:
        return Fibonacci(Num - 1) + Fibonacci(Num - 2)

for i in range(11):
    print("費波那契數 Fib(", str(i), ") = ", Fibonacci(i), sep = '')