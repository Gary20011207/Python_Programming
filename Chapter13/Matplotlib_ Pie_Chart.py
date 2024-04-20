# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

activities = ["work", "sleep", "Internet", "others"] # 活動的名稱
hours = [8, 7, 2, 7] # 活動的時間
colors = ["lightgreen", "lightblue", "yellow", "pink"] # 扇形的色彩
# 繪製圓形圖，其中explode參數會令第三個扇形分離開來，表示強調的意思
plt.pie(hours, labels = activities, colors = colors, shadow = True,
explode = (0, 0, 0.1, 0), autopct = "%1.1f%%")
# 設定以相同的寬高比例繪製圓形圖會比較美觀
plt.axis("equal")
plt.show()