# -*- coding: utf-8 -*-
# 給定海佛烈克極限、細胞平均汰換週期（線性），計算預期壽命以及單一細胞平均分裂數量（指數性）
def LifeTime(Hayflick_Limit, Cycle):
    print("預期壽命為：", Cycle * (Hayflick_Limit + 1), "年")
    Counter = 1
    for i in range(0, Hayflick_Limit + 1):
        Counter *= 2
    print("單一細胞平均分裂數量為：", Counter, "個")

Hayflick_Limit, Cycle = eval(input("請輸入海佛烈克極限（整數次）、細胞平均汰換週期（年），並以','區分兩者："))
LifeTime(Hayflick_Limit, Cycle)