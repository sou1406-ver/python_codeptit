from collections import Counter

for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    cnt=Counter(a)
    for i in a:
        if cnt[i]%2!=0:
            print(i)
            break