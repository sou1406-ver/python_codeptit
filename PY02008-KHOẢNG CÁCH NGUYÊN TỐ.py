import math

def ngto(n):
    if n<2: return False
    if n==2 or n==3: return True
    if n%2 ==0: return False
    for i in range(3, math.isqrt(n)+1,2):
        if n % i == 0: return False
    return True

def sinh(n):
    tmp=2
    h=[]
    while n>0:
        if ngto(tmp):
            h.append(tmp)
            n-=1
        tmp+=1
    return h

n,x=map(int,input().split())
h=sinh(n)
h1=[]
h1.append(x)
for i in range(n):
    h1.append(h1[i]+h[i])
print(*h1)