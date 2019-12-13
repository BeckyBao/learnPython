#!/usr/bin/python
# -*- coding: UTF-8 -*-

#input("按下 enter 键退出，其他任意键显示...\n")

#name = input("请输入用户名：")
#if name == "admin":
#    print("欢迎光临！")

'''
#练习1
num = input("请输入一个整数：")
if int(num) % 2 == 0:
    print("输入的为一个偶数")
else :
    print("输入的是一个奇数")
'''
'''
#练习二
year = int(input("请输入一个年份："))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 ):
    print("输入的是一个闰年")
else :
    print("输入的不是一个闰年")
'''
'''
#练习三
age = input("请输入狗狗的年龄：")
if 0<int(age) <= 2:
    print("您的小狗今年",float(age) *10.5,"岁啦")
else :
    print("您的小狗今年", 2 * 10.5 + 4*(int(age) - 2), "岁啦")
'''
'''
#练习4
grade = float(input("请输入小明的期末成绩(0-100)："))
if 0<= grade <=100:
    if rade == 100:
        print("奖励一辆BMW")
    elif 80 <= grade <= 99:
        print("奖励一台iphone")
    elif 60 <= grade <= 79:
        print("奖励一本参考书")
    else:
        print("啥也没有")
else:
    print("请输入合法成绩")
'''
'''
#练习5
high = input("您的身高（cm）：")
money = input("您的资产（万元）：")
handsome = input("对自己外貌的评分：")
if float(high) > 180 and float(money)>1000 and float(handsome)>500:
    print("我一定要嫁给他")
elif float(high) > 180 or float(money)>1000 or float(handsome)>500:
    print("嫁吧，比上不足，比下有余")
else:
    print("不嫁")
'''
#循环语句
'''
#练习1
sum = 0
num = 0
while  0<= num <=100:
    if(num % 2 != 0):
        sum = num +sum
    num += 1
print("100以内的奇数和为：",sum) #2500
#练习2
sum = 0
num = 1
numSum = 0
while num < 100:
    if(num % 7 == 0):
        numSum +=1
        sum = num +sum
    num += 1
print("100以内的7的倍数的和为：",sum,"个数为：",numSum) #735 14
#练习3
sum = 0
num = 100
print("1000以内的水仙花数有：\n")
while   num < 1000:
    if(100 <= num <= 999 ):
       # sum = (int(num / 100)) ** 3 + (int(num % 100 / 10) )** 3 + (int(num % 10)) **
        sum = (num // 100) ** 3 + (num % 100 // 10) ** 3 + (num % 10) ** 3
    if (sum == num):
         print(num, "\n")
    num += 1
 #153 370 371 407
#练习4
num = int(input("请输入一个数："))
num2 = 2
while (num2 < num):
    if(num % num2 == 0):
        print("您输入的数不是一个质数")
        break
    num2 += 1
else :print("您输入的数是一个质数")
#循环嵌套
#练习1
m = 1
while(m <= 9):
    n = 1
    while( n <= m ):
        print(f"{n} * {m} = {n*m}  ",end='')
        n += 1
    print("")
    m += 1
#练习2
from time import *
begin = time()
num = 3
print("100以内的质数有：")
while (num < 10000):
    num2 = 2
    while (num2 < num ** 0.5):
        if (num % num2 == 0):
            break
        num2 += 1
    else:
        print(num)
    num += 1
end = time()
print("执行程序花费了",end-begin,"秒")
'''



