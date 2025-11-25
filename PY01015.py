def check(n):
    for i in range(1, len(n)) :
        if int(n[i]) < int(n[i-1]):
            return False
    return True
t =int(input())
for _ in range(t):
    n=input()
    if check(n): print("YES")
    else: print("NO")
