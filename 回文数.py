# -*- coding: utf-8 -*-
#一个5位数，判断它是不是回文数。
#while 循环
x = input("请输入一个五位数")

while 1:
    if x[0] == x[4] and x[1] == x[3]:
        print("这是一个回文数")
        break
    else:
        print("这不是一个回文数")
        break

print(x)

# for 循环

x = input("请输入一个五位数")
t = 0

for i in range(int(len(x)/2)):
    if x[i] != x[-i-1]:
        print("这不是一个回文数")
        t = 1
        break

if t == 0:
    print("这是一个回文数")




