def check(n):
    cnt=int(n[0])
    for i in range(1, len(n)) :
        cnt+=int(n[i])
        if abs(int(n[i]) - int(n[i-1])) != 2:
            return False
    if cnt%10==0: return True
    else: return False
t =int(input())
for _ in range(t):
    n=input()
    if check(n): print("YES")
    else: print("NO")
