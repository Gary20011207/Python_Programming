# -*- coding: utf-8 -*-
# 學習其他語法，包含pass以及assert
try:
    Num = eval(input("輸入數字0 ~ 9："))
    if Num >= 10 or Num < 0:
        assert False, "數字不在範圍內！" # 使用assert中斷的方法為「assert False, "錯誤訊息"」，用法和raise類似，執行後就會中斷程式，並將錯誤資訊提供給except顯示。
    print("數字為", Num)
except AssertionError as Message:
    print(Message)
except:
    pass # 在撰寫try...except有時候會遇到「不想做任何動作」的狀況，這時可以使用pass語法來略過（什麼事情都不做）
finally:
    print("程式結束！")