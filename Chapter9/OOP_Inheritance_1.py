# -*- coding: utf-8 -*-
class A: # 定義類別A
    __x = "我是屬性__x" # 定義私有屬性，無法被子類別繼承
    y = "我是屬性y" # 定義非私有屬性，能夠被子類別繼承

    def __M1(self): # 定義私有方法，無法被子類別繼承
        print("我是方法M1()")

    def M2(self): # 定義非私有方法，能夠被子類別繼承
        print("我是方法M2()")

class B(A): # 定義類別B繼承自類別A
    z = "我是屬性z"

    def M3(self):
        print("我是方法M3()")