import math


def ngto(n):
    if n<2: return False
    if n==2 or n==3: return True
    if n%2 ==0: return False
    for i in range(3, math.isqrt(n)+1,2):
        if n % i == 0: return False
    return True

for _ in range(int(input())):
    s=input()
    n1=n2=0
    for i in range(len(s)):
        if ngto(int(s[i])): n1+=1
        else : n2+=1
    if ngto(len(s)) and n1>n2: print("YES")
    else: print("NO")