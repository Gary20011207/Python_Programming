# -*- coding: utf-8 -*-
list1 = []

for i in range(1, 6):
    prompt = "請輸入第" + str(i) + "位評審的分數："
    score = eval(input(prompt))
    list1.append(score)

print("這位選手的總分為", sum(list1))