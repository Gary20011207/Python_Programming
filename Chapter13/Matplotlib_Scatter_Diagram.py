# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

HW = np.loadtxt("C:\\Users\\chen_\\Desktop\\MyProject\\Python_Project\\Python程式設計（第三版）\\Chapter13\\HW.txt", delimiter = ",") # 從HW.txt檔案載入身高與體重資料
Heights = HW[:, 0] # 將第一行的身高資料指派給Heights
Weights = HW[:, 1] # 將第二行的體重資料指派給Weights
plt.scatter(Heights, Weights) # 根據身高與體重資料繪製散佈圖
plt.xlabel("Heights (cm)")
plt.ylabel("Weights (kg)")
plt.show()