for _ in range(int(input())):
    s1=input()
    s2=input()
    cnt=0
    s3=s1.replace(s2,"")
    while s1!=s3:
        s1.replace(s2,'')
        cnt+=1
    print(cnt)