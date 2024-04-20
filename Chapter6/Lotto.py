# -*- coding: utf-8 -*-
import random

lotto = []

for i in range(6):
    lotto.append(random.choice([x for x in range(1, 50) if x not in lotto]))

lotto.sort()
print(lotto)