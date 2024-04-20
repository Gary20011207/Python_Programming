# -*- coding: utf-8 -*-
'''
令使用者輸入欲猜的數字範圍，
隨機產生一個範圍內的數字，
接著開始重複執行猜數字，
程式會告知使用者輸入的數字太大或太小，
當相等時會結束程式，
並顯示使用者猜了幾次。
'''
import random as rd

min, max = eval(input("請輸入欲猜的數字範圍，並以','區分兩者："))
Ans = rd.randint(min, max)

Guess_Times = 0

while(True):
    Guess_Num = eval(input("請猜數字："))
    Guess_Times += 1

    if(Guess_Num == Ans):
        print("猜對了!", "使用者共猜了", Guess_Times, "次")
        break

    elif(Guess_Num > Ans):
        print("猜的太大了!")

    elif(Guess_Num < Ans):
        print("猜的太小了!")