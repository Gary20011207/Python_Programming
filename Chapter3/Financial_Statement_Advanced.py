# -*- coding: utf-8 -*-
# 給定欲紀錄年份數量，並給定每年年度、營業額、成本，計算獲利率（至小數點第二位），並印出財務報表
Year = eval(input("請輸入欲紀錄年份數量："))
Each_Year = []
Revenue = []
Cost = []
Profit_Margin = []

for i in range(1, Year + 1):
    Temp_Each_Year, Temp_Revenue, Temp_Cost = eval(input("請輸入第 {0} 年度、營業額、成本，並以','區分三者：".format(i)))

    if Temp_Revenue < Temp_Cost: # 獲利率 < 0%
        Temp_Profit_Margin = -1 * ((Temp_Cost - Temp_Revenue) / Temp_Revenue)
    elif Temp_Revenue >= Temp_Cost: # 獲利率 >= 0%
        Temp_Profit_Margin = ((Temp_Revenue - Temp_Cost) / Temp_Cost)

    Each_Year.append(Temp_Each_Year)
    Revenue.append(Temp_Revenue)
    Cost.append(Temp_Cost)
    Profit_Margin.append(Temp_Profit_Margin)

print("{0:^10}{1:^10}{2:^10}{3:^10}".format("年度", "營業額", "成本", "獲利率"))
for i in range(0, Year):
    print("{0:^12}{1:^12,}{2:^12,}{3:^14.2%}".format(str(Each_Year[i]), Revenue[i], Cost[i], Profit_Margin[i]))