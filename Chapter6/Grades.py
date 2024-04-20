# -*- coding: utf-8 -*-
grades = [[95, 100, 100], [86, 90, 75], [98, 98, 96], [78, 90, 80], [70, 68, 72]]
for i in range(5):
    subTotal = 0
    for j in range(3):
        subTotal += grades[i][j]
    grades[i].append(subTotal)

for i in range(5):
    print("學生", i + 1, "的總分為", grades[i][3])