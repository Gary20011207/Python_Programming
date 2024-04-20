# -*- coding: utf-8 -*-
EnglishNum = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]

num = eval(input("請輸入1 ~ 5的整數："))

if num in range(1, 6):
    print(EnglishNum[num - 1])
else:
    print("您輸入的資料超過範圍！")