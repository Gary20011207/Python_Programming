# -*- coding: utf-8 -*-
def matrixMul(A, B):
    C = []
    if len(A[0]) != len(B): # 僅偵錯起始條件
        print("這兩個矩陣不能相乘！")
        exit()

    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append(0)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = '\t')
        print('\n')

A = [[1, 2], [3, 4], [5, 6]]
B = [[1, 2, 3], [4, 5, 6]]

C = matrixMul(A, B)

print("這兩個矩陣相乘的結果如下：\n")
printMatrix(C)