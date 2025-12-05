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
    sum=0
    for i in range(len(n)):
        sum+=int(n[i])
    if ngto(sum): print("YES")
    else: print("NO")