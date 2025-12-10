def tcs(n):
    return sum(int(i) for i in n)

for _ in range(int(input())):
    n = int(input())
    a=[x for x in input().split()]
    a.sort(key= lambda x:(tcs(x), int(x)))
    print(*a)
