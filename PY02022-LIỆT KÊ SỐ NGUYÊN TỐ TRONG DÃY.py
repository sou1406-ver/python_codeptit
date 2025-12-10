import math

def ngto(n):
    if n<2: return False
    if n==2 or n==3: return True
    if n%2 ==0: return False
    for i in range(3, math.isqrt(n)+1,2):
        if n % i == 0: return False
    return True


n=int(input())
a=[int(a) for a in input().split()]
b=[]
for i in a:
    if ngto(i) and i not in b:
        print(i, a.count(i), sep=' ')
        b.append(i)