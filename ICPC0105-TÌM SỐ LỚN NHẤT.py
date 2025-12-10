for _ in range(int(input())):
    n=input().strip()
    b=[]
    i=0
    s=""
    while i<len(n):
        while i<len(n) and  n[i].isdigit():
            s+=n[i]
            i+=1
        if s:
            b.append(int(s))
            s=""
        i+=1
    print(max(b))