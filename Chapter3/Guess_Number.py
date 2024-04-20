# -*- coding: utf-8 -*-
# Guess Number 1 ~ 3
import random

num = random.randint(1, 3)

Ans = eval(input("請猜數字1 ~ 3："))

print(num, "==", Ans, "is", num == Ans)