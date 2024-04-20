# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 將常態分佈的期望值與標準差設定為0, 1（即標準常態分佈）
loc, scale = 0, 1
# 變數x是用來繪製機率密度函數的資料（從1% ~ 99%之間平均取出100個值）
x = np.linspace(stats.norm.ppf(0.01, loc, scale), stats.norm.ppf(0.99, loc, scale), 100)
# 以紅色實線繪製標準常態分佈的機率密度函數
plt.plot(x, stats.norm.pdf(x), "r-", label = "norm pdf")

# 產生1000個標準常態分佈亂數
r = stats.norm.rvs(size = 1000)
# 將1000個亂數繪製成直方圖（透明度設定為0.2）
plt.hist(r, density = True, histtype = "stepfilled", alpha = 0.2)
# 顯示圖例
plt.legend()
plt.show()