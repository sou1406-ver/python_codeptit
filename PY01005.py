n = int(input())
cnt = 0
while n>10:
    if n%10==4 or n%10==7:
        cnt+=1
    n//=10
if n==4 or n==7: cnt+=1
if cnt ==4 or cnt==7: print("YES")
else:print("NO")
