import math

def ngto(n):
    if n<2: return False
    if n==2 or n==3: return True
    if n%2 ==0: return False
    for i in range(3, math.isqrt(n)+1,2):
        if n % i == 0: return False
    return True

for _ in range(int(input())):
    n=input()
    if ngto(int(n[-3:])) and ngto(int(n[:3])): print("YES")
    else: print("NO")