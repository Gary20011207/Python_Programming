# -*- coding: utf-8 -*-
# 學習Lambda的其他應用方式

# Short Function
from numpy import number


multiply = lambda x, y: x * y
print(multiply(4, 2))

# Filter
numbers = [50, 2, 12, 30, 27, 4]

result = filter(lambda x: x > 10, numbers)
print(list(result))

# Map
result = map(lambda x: x * 2, numbers)
print(list(result))

# Reduce
from functools import reduce
result = reduce(lambda x, y: x + y, numbers)
print(result)

# Sorted
cars = [("Mazda", 2000),
        ("Toyota", 1000),
        ("Benz", 5000)]

result = sorted(cars, key = lambda car: car[1])
print(result)

'''
這邊來比較一下Lambda函式與一般函式(Function)的差異為：
1. Lambda函式不需要定義名稱，而一般函式(Function)需定義名稱。
2. Lambda函式只能有一行運算式，而一般函式(Function)可以有多行運算式。
3. Lambda在每一次運算完會自動回傳結果，而一般函式(Function)如果要回傳結果要加上 return 關鍵字。

以上就是今天Python Lambda函式使用上的觀念與技巧，從範例中可以看到，
在Python內建函式中使用Lambda函式非常的強大，適度的使用讓程式碼簡潔了許多。
不過也建議避免過度使用與撰寫複雜的Lambda函式，不然程式碼將不易維護，
複雜的邏輯運算，還是優先選擇一般函式(Function)較為理想。
'''

# Complex Lambda
Japanese = {
'a':'あ','i':'い',"shi":'し',"te":'て',"ru":'る'
}
Test = ['a', 'i', "shi", "te", "ru"]
for i in range(0, 5):
    (lambda str: print(Japanese[str], end = ''))(Test[i])