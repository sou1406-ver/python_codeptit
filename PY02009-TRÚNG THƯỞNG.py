from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a=[int(input()) for _ in range(n)]
    a.sort()
    cnt=Counter(a)
    ts_max=max(cnt.values())
    c=[v for v,f in cnt.items() if f==ts_max]
    print(min(c))