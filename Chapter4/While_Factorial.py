# -*- coding: utf-8 -*-
num = eval(input("請輸入1 ~ 10的正整數："))

result = 1

i = 1

while i <= num:
    result = result * i
    i = i + 1

print("{0}階乘為{1}".format(num, result))