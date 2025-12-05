for _ in range(int(input())):
    n=input()
    sum=1
    for i in range(len(n)):
        if n[i]!='0':
            sum*=int(n[i])
    print(sum)