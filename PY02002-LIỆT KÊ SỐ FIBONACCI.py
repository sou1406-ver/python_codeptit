for _ in range(int(input())):
    a, b = map(int, input().split())
    c=[0]*105
    c[1]=c[2]=1
    for i in range(3, 101):
        c[i]=c[i-1]+c[i-2]
    for i in range(a, b+1):
        print(c[i], end=' ')
    print()