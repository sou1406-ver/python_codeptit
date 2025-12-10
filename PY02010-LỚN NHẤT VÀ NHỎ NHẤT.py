while True :
    n=int(input())
    if n==0:
        break
    b=[]
    for i in range(n):
        a=input().lstrip('0')
        if a=='':a='0'
        b.append(a)
    if len(set(b))==1:
        print('BANG NHAU')
        continue
    b.sort(key=lambda x:(len(x), x))
    print(b[0], b[-1], sep=' ')
