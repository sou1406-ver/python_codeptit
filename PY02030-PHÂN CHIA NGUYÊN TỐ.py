import math

def ngto(n):
    if n<2: return False
    if n==2 or n==3: return True
    if n%2 ==0: return False
    for i in range(3, math.isqrt(n)+1,2):
        if n % i == 0: return False
    return True

n=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in a:
    if b.count(i)==0:
        b.append(i)
tong_sau=sum(b)
tong_trc=0
for i in range(len(b)):
    tong_sau-=b[i]
    tong_trc+=b[i]
    if ngto(tong_trc) and ngto(tong_sau) :
        print(i)
        break
if tong_sau==0:print('NOT FOUND')