n = int(input())
a = []
while len(a)<n:
    a.extend(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]%2==0 and a[j]%2==0 and a[i]>a[j]:
                  a[i],a[j]=a[j],a[i]
        if a[i]%2!=0 and a[j]%2!=0 and a[i]<a[j]:
                    a[i],a[j]=a[j],a[i]
print(*a)