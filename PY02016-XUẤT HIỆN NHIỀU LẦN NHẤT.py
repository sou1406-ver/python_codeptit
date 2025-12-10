from collections import Counter

for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    cnt=Counter(a)
    b=sorted(a, key=lambda x:(-cnt[x],x))
    if a.count(b[0])> len(b)/2:
        print(b[0])
    else: print('NO')