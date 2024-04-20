# -*- coding: utf-8 -*-
from scipy.optimize import root

def f(x):
    return (2 * x ** 2 - 4 * x + 1)

def g(x):
    return (x - 2)

sol = root(lambda x: f(x) - g(x), 0) # 將初始猜測值設定為0去找交點
print(sol.x) # 印出最佳化的結果
print(f(sol.x)) # 將找到的x代入f(x)
print(g(sol.x)) # 將找到的x代入g(x)