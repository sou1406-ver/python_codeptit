import math

def ngto(n):
    if n<2: return False
    if n==2 or n==3: return True
    if n%2 ==0: return False
    for i in range(3, math.isqrt(n)+1,2):
        if n % i == 0: return False
    return True

def gannhat(n):
    if ngto(n): return 0
    up=n
    ucnt=0
    while not ngto(up):
        up+=1
        ucnt+=1
    down=n
    dcnt=0
    while not ngto(down):
        down-=1
        dcnt+=1
    return min(ucnt,dcnt)


n=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in a:
    cnt=gannhat(i)
    b.append(cnt)
print(max(b))