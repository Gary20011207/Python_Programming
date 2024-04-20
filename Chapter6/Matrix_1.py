# -*- coding: utf-8 -*-
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
'''
matrix = []
rows = eval(input("請輸入矩陣的列數："))
cols = eval(input("請輸入矩陣的行數："))

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        element = eval(input("請輸入矩陣的元素（由上往下逐列輸入）："))
        matrix[i].append(element)

print(matrix)