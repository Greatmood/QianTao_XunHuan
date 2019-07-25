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
