t = int(input())
for _ in range(t):
    s=input()
    s1=''
    for i in range(1,len(s),2):
        for j in range(1, int(s[i])+1 ):
            s1+=str(s[i-1])
    print(s1)