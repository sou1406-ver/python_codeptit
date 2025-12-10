for _ in range(int(input())):
    p,q=input().split()
    x1=input()
    if len(x1.split())>1:
        x1, x2 = x1.split()
    else :x2=input()
    a1={int(x1), int(x1.replace(p,q)), int(x1.replace(q,p))}
    a2={int(x2), int(x2.replace(p,q)), int(x2.replace(q,p))}
    xmax=max(a1)+max(a2)
    xmin=min(a1)+min(a2)
    print(xmin,xmax)

