a=[]
for _ in range(int(input())):
    s=input()
    s1=''
    for i in s:
        if i.isdigit(): s1+=i
        else:
            if s1!='':
                a.append(int(s1))
                s1=''
    if s1!='':
        a.append(int(s1))
    a.sort()
print(*a, sep='\n')
