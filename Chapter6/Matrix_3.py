# -*- coding: utf-8 -*-
def matrixAdd(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(0)

    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = '\t')
        print('\n')

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

C = matrixAdd(A, B)

print("這兩個矩陣相加的結果如下：\n")
printMatrix(C)