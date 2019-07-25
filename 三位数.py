# -*- coding: utf-8 -*-

#.有1，2，3，4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
#for循环
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):
                print(str(i)+str(j)+str(k),sep="",end="|")
                count += 1
print()
print("%d"%(count))

#while 循环
a,n = 0,0
while a < 4:
    a += 1
    b = 0
    while b < 4:
        b += 1
        c = 0
        while c < 4:
            c += 1
            if (a != b) and (b != c) and (c != a):
                n += 1
                print(a,b,c,sep="",end="|")
print()
print(n)
