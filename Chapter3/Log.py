# -*- coding: utf-8 -*-
# While x = log2, y = log3, Calculate 10^(2x + 3y + 1)
import math

x = math.log(2, 10)
y = math.log(3, 10)

Ans = pow(10, 2 * x + 3 * y + 1)
print("結果為：", Ans)