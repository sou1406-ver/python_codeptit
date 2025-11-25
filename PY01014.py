a, k, n= [int(x) for x in input().split()]
arr=[]
for i in range(k, n+1, k):
    b= i-a
    if b>0: arr.append(b)
if len(arr)>0: print(*arr)
else: print('-1')
