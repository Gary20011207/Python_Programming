# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.square(x)
plt.plot(x, y, "ro") # 加入第三個參數"ro"，改用紅色圓形標記繪製x與y
plt.show()