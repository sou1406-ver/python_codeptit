for t in range(int(input())):
    s=input()
    tong=0
    a=[]
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':  tong += int(s[i])
        else : a.append(s[i])
    a.sort()
    print(''.join(a)+str(tong))