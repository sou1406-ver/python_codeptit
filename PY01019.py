for t in range(int(input())):
    s=input()
    s1=s[::-1]
    ok= True
    for i in range(1, len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(s1[i]) - ord(s1[i-1])):
            ok=False
            break
    if ok :print("YES")
    else:print("NO")