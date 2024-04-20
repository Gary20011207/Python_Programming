# -*- coding: utf-8 -*-
from scipy.optimize import root

def fun(x):
    return [2 * x[0] + x[1] - 5, x[0] - 3 * x[1] + 1]

sol = root(fun, [0, 0]) # 將x[0], x[1]的初始猜測值設定為0, 0去求解
print(sol.x) # 印出最佳化的結果