# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.xlabel("Age") # 將X軸的標籤設定為"Age"（年齡）
plt.ylabel("Monthly Salary") # 將Y軸的標籤設定為"Monthly Salary"（月薪）
plt.xticks(np.arange(7), ("", "<=20", "21~30", "31~40", "41~50", ">=51", ""))
plt.yticks(np.arange(6), ("", "<25K", "25K~35K", "35K~45K", ">45K", ""))
plt.minorticks_on() # 顯示子刻度
plt.show()