# -*- coding: utf-8 -*-
import os.path
import sys

sourcefile = input("請輸入來源檔案名稱（*.txt）：")
targetfile = input("請輸入目的檔案名稱（*.txt）：")

if os.path.isfile("C:\\Users\\chen_\\Desktop\\MyProject\\Python_Project\\Python程式設計（第三版）\\Chapter7\\" + targetfile): # 若目的檔案已經存在，就取消複製並結束程式
    print("目的檔案已經存在，取消複製檔案！")
    sys.exit()

fileObject1 = open("C:\\Users\\chen_\\Desktop\\MyProject\\Python_Project\\Python程式設計（第三版）\\Chapter7\\" + sourcefile, "r")
fileObject2 = open("C:\\Users\\chen_\\Desktop\\MyProject\\Python_Project\\Python程式設計（第三版）\\Chapter7\\" + targetfile, "w")
content = fileObject1.read() # 讀取來源檔案的所有內容
fileObject2.write(content) # 將所有內容寫入目的檔案
fileObject1.close()
fileObject2.close()
print("檔案複製完畢！")