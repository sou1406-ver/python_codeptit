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
for i in range(n):
    for j in  range(i+1, n):
        if ngto(a[i]) and ngto(a[j]) and a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
print(*a)