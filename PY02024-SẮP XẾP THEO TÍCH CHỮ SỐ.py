def tcs(n):
    tich=1
    for i in n :
        tich*=int(i)
    return tich

for _ in range(int(input())):
    n = int(input())
    a=[x for x in input().split()]
    a.sort(key= lambda x:(tcs(x), int(x)))
    print(*a)
