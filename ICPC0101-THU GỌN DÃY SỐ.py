n = int(input())
a = list(map(int, input().split()))
b=[]
for i in a:
    if len(b)==0:
        b.append(i)
    elif (i+ b[-1])%2==0:
        b.pop()
    else: b.append(i)
print(len(b))