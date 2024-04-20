# -*- coding: utf-8 -*-
def CtoF1(degreeC):
    degreeF = degreeC * 1.8 + 32
    print("攝氏", degreeC, "度可以轉換成華氏", degreeF, "度")

temperatureC = eval(input("請輸入攝氏溫度："))

CtoF1(temperatureC)