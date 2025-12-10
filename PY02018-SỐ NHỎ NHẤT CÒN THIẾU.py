n=int(input())
a=sorted([int(x) for x in input().split()])
ok=True
tmp=a[-1]+1
for i in range(len(a)-1):
    if a[i]+1 !=a[i+1]:
        ok=False
        tmp=a[i]+1
        break
print(tmp)
