# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100) # 建立-10到10之間100個平均分佈的數值
y1 = 20 * np.sin(x) # 設定函數y1 = 20 * sin(x)
y2 = x * x * np.cos(x) + 0.5 # 設定函數y2 = x^2 * cos(x) + 0.5
plt.subplot(211) # 在2列1行的第1張子圖表進行繪圖
plt.plot(x, y1, "b-") # 繪製函數y1 = 20 * sin(x)
plt.subplot(212) # 在2列1行的第2張子圖表進行繪圖
plt.plot(x, y2, "r--") # 繪製函數y2 = x^2 * cos(x) + 0.5
plt.show()