from collections import Counter

n, m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
cnt = Counter(a)
a.sort(key=lambda x: (cnt[x], -x))
if len(set(a)) <2:
    print('NONE')
else:
    ts_max= max(cnt.values())
    b=[x for x in set(cnt.values()) if x < ts_max]
    if len(b) <2:
        print('NONE')
    else:
        ans=max(b)
        for i in a[::-1]:
            if cnt[i]==ans:
                print(i)
                break