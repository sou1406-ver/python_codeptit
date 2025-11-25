import math

t=int(input())
def ngto(n):
    if n<2: return False
    if (n==2) or (n==3): return True
    if n % 2 == 0: return False
    for i in range(3, math.isqrt(n),2):
        if n % i == 0: return False
    return True
for _ in range(t):
    a,b = input().split()
    cnt=0
    k=math.gcd(int(a),int(b))
    while k > 0:
        cnt += k%10
        k//=10
    if(ngto(cnt)): print("YES")
    else: print("NO")