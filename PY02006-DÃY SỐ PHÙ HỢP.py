for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    ok=True
    a.sort()
    b.sort()
    for i in range(n):
        if a[i]>b[i]:
            ok=False
            break
    if ok:
        print('YES')
    else:
        print('NO')