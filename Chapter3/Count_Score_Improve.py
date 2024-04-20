# -*- coding: utf-8 -*-
# 給定任意科目數、該科分數與學分數，計算總平均
Subject_Number = eval(input("請輸入科目數："))

Total_Credits = 0
Total_Score = 0

for i in range(0, Subject_Number):
    Score, Credits = map(float, input("請輸入第 {0} 科分數與學分數，並以空格區分兩者：".format(i)).split())
    Total_Score += Score * Credits
    Total_Credits += Credits

print("學期總平均為：", Total_Score / Total_Credits)