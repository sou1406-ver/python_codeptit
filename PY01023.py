import math

for t in range(int(input())):
    n= int(input())
    kq=[]
    kq.append('1')
    for i in range(2, math.isqrt(n)+1):
        cnt=0
        while n%i == 0:
            cnt+=1
            n//=i
        if cnt>0: kq.append(f"{i}^{cnt}")
    if n>1: kq.append(f"{n}^{1}")
    print(" * ".join(kq))