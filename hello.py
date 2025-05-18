python从零开始学习笔记

变量：
name = "Wendy"
age = 29

print("Hello, my name is", name)
print("I am", age, "years old.")

数据类型与输入
input() 函数：让用户输入内容
name = input("What's your name? ")
这个函数会显示提示文字，等用户输入后把输入保存到变量中

数据类型转换：
用户输入的所有东西，默认都是字符串（文字），比如：
age = input("How old are you? ")

即使你输入了数字 25，Python 也会把它当作 "25"（字符串）来看。
如果我们想进行数字计算，就要把它变成数字类型：
age = int(input("How old are you? "))  # 转换为整数
height = float(input("Your height in meters? "))  # 转换为小数

name = input("What's your name? ")
age = int(input("How old are you? "))
height = float(input("Your height in meters? "))

print("Hello,", name + "!")
print("You are", age, "years old.")
print("Your height is", height, "meters.")

weight = float(input("Your weight in kg? "))
bmi = weight / (height ** 2)
print("Your BMI is", bmi)

第四课：条件判断（if / else）
if 条件:
    做这个事情
else:
    做另一个事情
  
  age = 20       （ 建议保留空一行来让代码更清晰、更易读

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
