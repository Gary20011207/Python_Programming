# -*- coding: utf-8 -*-
import random
num = random.randint(1, 10)
answer = -1 # 變數answer的初始值設定為-1，表示尚未輸入

while answer != num:
    answer = eval(input("請猜數字1 ~ 10："))
    if answer > num:
        print("太大了！")
    elif answer < num:
        print("太小了！")
    else:
        print("猜對了！")