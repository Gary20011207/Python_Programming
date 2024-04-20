# -*- coding: utf-8 -*-
fileObject = open("C:\\Users\\chen_\\Desktop\\MyProject\\Python_Project\\Python程式設計（第三版）\\Chapter7\\Poem_1.txt", "r")

'''
line = fileObject.readline() # 讀取一行
while line != '': # 檢查是否抵達檔案結尾
    print(line)
    line = fileObject.readline() # 讀取下一行
'''

for line in fileObject: # 使用for迴圈印出每一行
    print(line)

fileObject.close()