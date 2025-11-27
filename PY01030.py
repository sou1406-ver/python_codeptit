import math

a, b= [int(x) for x in input().split() ]
c=[]
for i in range(10**(b-1), 10**b):
    if math.gcd(i, a) == 1:
        c.append(i)
for i in range (0, len(c),10):
    print(*c[i:i+10])