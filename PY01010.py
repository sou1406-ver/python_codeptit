t=int(input())
for _ in range(t):
    n=input()
    if int(n[:2]) == int(n[-2:]): print("YES")
    else: print("NO")