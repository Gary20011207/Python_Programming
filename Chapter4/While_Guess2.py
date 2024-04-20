# -*- coding: utf-8 -*-
answer = input("請輸入「快樂」的英文：")

while answer.upper() != "HAPPY":
    if answer.upper() == "QUIT":
        print("我不玩了！")
        break
    answer = input("答錯了，請重新輸入「快樂」的英文：")
else:
    print("答對了！")