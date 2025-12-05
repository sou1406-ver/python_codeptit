for _ in range(int(input())):
    n=input()
    sum=0
    for i in range(len(n)):
        sum+=int(n[i])
    if sum%3==0: print("YES")
    else: print("NO")