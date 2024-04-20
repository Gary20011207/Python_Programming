# -*- coding: utf-8 -*-
from scipy.optimize import root

def f(x):
    return (2 * x ** 2 - 4 * x + 1)

sol1 = root(f, 0) # 將初始猜測值設定為0去求根
print(sol1.x) # 印出最佳化的結果
sol2 = root(f, 1) # 將初始猜測值設定為1去求根
print(sol2.x) # 印出最佳化的結果
sol3 = root(f, 2) # 將初始猜測值設定為2去求根
print(sol3.x) # 印出最佳化的結果

'''
import numpy as np
r = np.roots([2, -4, 1]) # 參數為函數的係數（降冪排列），缺項為0
print(r) # 找到兩個根
'''