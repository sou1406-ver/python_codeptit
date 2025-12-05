for t in range(int(input())):
    n=input()
    if len(set(n))==2 and len(set(n[::2]))==1 and len(set(n[1::2]))==1:
        print('YES')
    else:
        print('NO')
