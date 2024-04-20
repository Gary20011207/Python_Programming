# -*- coding: utf-8 -*-
class ShoppingCar():
    # 這個初始化方法用來設定購物車的所有人與商品（初始值為空串列）
    def __init__(self, owner):
        self.__owner = owner
        self.__product = []

    # 這個方法用來傳回購物車的所有人
    def getOwner(self):
        return self.__owner
    
    # 這個方法用來將參數product所指定的商品放入購物車
    def addProduct(self, product):
        self.__product.append(product)

    # 這個方法用來從購物車移除參數product所指定的商品
    def removeProduct(self, product):
        self.__product.remove(product)

    # 這個方法用來傳回購物車內的商品
    def getProduct(self):
        return self.__product

# 建立一個購物車物件，所有人為"小丸子"
obj = ShoppingCar("小丸子")
# 將巧克力放入購物車
obj.addProduct("巧克力")
# 將咖啡豆放入購物車
obj.addProduct("咖啡豆")
# 將馬卡龍放入購物車
obj.addProduct("馬卡龍")
# 將草莓果醬放入購物車
obj.addProduct("草莓果醬")
# 將手工餅乾放入購物車
obj.addProduct("手工餅乾")
# 從購物車移除咖啡豆
obj.removeProduct("咖啡豆")
# 印出購物車的所有人與裡面的商品
print(obj.getOwner(), "的購物車裡面有", obj.getProduct())