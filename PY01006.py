for t in range(int(input())):
    n = int(input())
    ok=True
    while n > 0:
        if n%10 != 4 and n%10 != 7:
            ok=False
        n//=10
    if ok: print("YES")
    else:print("NO")