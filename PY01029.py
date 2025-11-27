import math

for t in range(int(input())):
    n=int(input())
    rn=int(str(n)[::-1])
    if math.gcd(n, rn)==1:
        print('YES')
    else:
        print('NO')