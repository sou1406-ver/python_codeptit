import math

tong=0
for _ in range(int(input())):
    n=int(input())
    while n % 2 == 0:
        n//=2
        tong+=2
    for i in range(3, math.isqrt(n)+1,2):
        while n % i == 0:
            n //= i
            tong+=i
    if n>1: tong+=n
print(tong)