# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("C:\\Users\\chen_\\Desktop\\MyProject\\Python_Project\\Python程式設計（第三版）\\Chapter15\\iris.csv", names = ["SepalL", "SepalW", "PetalL", "PetalW", "Class"])
# 取出品種為Iris-setosa的資料
iris1 = iris[iris["Class"] == "Iris-setosa"]
# 取出品種為Iris-versicolor的資料
iris2 = iris[iris["Class"] == "Iris-versicolor"]
# 取出品種為Iris-virginica的資料
iris3 = iris[iris["Class"] == "Iris-virginica"]
plt.scatter(iris1["SepalL"], iris1["SepalW"], c = "red", marker = 'o', label = "setosa")
plt.scatter(iris2["SepalL"], iris2["SepalW"], c = "green", marker = 'D', label = "versicolor")
plt.scatter(iris3["SepalL"], iris3["SepalW"], c = "blue", marker = 'x', label = "virginica")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend()
plt.show()