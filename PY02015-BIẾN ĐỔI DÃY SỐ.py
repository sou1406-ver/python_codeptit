while True:
    a=[int(x) for x in input().split()]
    if a==[0]*4:
        break
    tmp=a.copy()
    cnt=0
    while len(set(a)) !=1:
        for i in range(3):
            tmp[i]=abs(a[i]-a[i+1])
        tmp[3]=abs(a[3]-a[0])
        cnt+=1
        a=tmp.copy()
    print(cnt)