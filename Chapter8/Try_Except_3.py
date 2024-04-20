# -*- coding: utf-8 -*-
while True:
    try:
        fileName = input("請輸入檔案名稱：")
        fileObject = open("C:\\Users\\chen_\\Desktop\\MyProject\\Python_Project\\Python程式設計（第三版）\\Chapter8\\" + fileName, "r")
        break
    except FileNotFoundError:
        print("找不到檔案！")

content = fileObject.read()
print(content)
fileObject.close()