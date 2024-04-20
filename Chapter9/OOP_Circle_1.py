# -*- coding: utf-8 -*-
class Circle:
    PI = 3.14
    radius = 1

    def getArea(self):
        return self.PI * self.radius * self.radius

C1 = Circle() # 建立一個物件並指派給C1
print("半徑為", C1.radius, "的圓面積為", C1.getArea()) # 印出C1的半徑與圓面積

C2 = C1 # 令C2參照C1所參照的物件
C2.radius = 10 # 將C2的半徑設定為10
print("半徑為", C1.radius, "的圓面積為", C1.getArea()) # 印出C1的半徑與圓面積