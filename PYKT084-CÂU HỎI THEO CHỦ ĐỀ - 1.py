a=[]
for _ in range(int(input())): a.append(input())
while len(a)>0:
    cnt=len(a)
    for s in a:
        if s=='':
            cnt=a.index(s)
            break
    print(f'{a[0]}: {cnt-1}')
    a=a[cnt+1:]


