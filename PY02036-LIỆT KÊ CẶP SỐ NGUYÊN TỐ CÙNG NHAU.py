from  math import gcd

n=int(input())
a=sorted([int(x) for x in input().split()])
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if gcd(a[i],a[j])==1:
            print(a[i], a[j], sep=' ')
