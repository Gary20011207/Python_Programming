# -*- coding: utf-8 -*-
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = '\t')
        print('\n')

printMatrix(matrix)