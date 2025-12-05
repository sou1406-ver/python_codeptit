#test yếu ko có th tất cả lẻ =1
for _ in range(int(input())):
    n=input()
    tong=0
    tich=1
    found=False
    for i in range(len(n)):
        if i%2==1: tong+= int(n[i])
        if i%2==0 and int(n[i])!=0: tich*=int(n[i])
    for i in range(len(n)):
        if i%2==0 and int(n[i])!=0:
            found=True
    if tich==1 and not found:tich=0
    print(tich, tong, sep=' ')