# -*- coding: utf-8 -*-
class Employee:
    # 這個初始化方法用來設定員工的姓名
    def __init__(self, name):
        self.__name = name

    # 這個方法用來傳回員工的姓名
    def getName(self):
        return self.__name

    # 這個方法用來傳回員工的本月薪水
    def getSalary(self, hours, payrate):
        return hours * payrate

class SalesPerson(Employee):
    # 這個方法用來傳回銷售人員的本月薪水（含業績獎金）
    def getSalary(self, hours, payrate, bonus):
        return hours * payrate + bonus

E1 = Employee("小丸子")
E2 = SalesPerson("小紅豆")
print("員工", E1.getName(), "的本月薪水為", E1.getSalary(120, 150))
print("銷售人員", E2.getName(), "的本月薪水為", E2.getSalary(120, 150, 3000))