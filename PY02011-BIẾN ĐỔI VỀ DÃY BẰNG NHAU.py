n=int(input())
a=[int(x) for x in input().split()]
kc=10000000000
tmp=0
for i in a:
    tong=0
    for j in a:
        tong+= abs(j-i)
    if kc > tong :
        tmp=i
        kc=tong
print(kc, tmp, sep=' ')