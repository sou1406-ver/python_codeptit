#test yếu ko có th tất cả lẻ =1
for _ in range(int(input())):
    n=input()
    tong=0
    tich=1
    for i in range(len(n)):
        if i%2==0: tong+= int(n[i])
        if i%2==1 and int(n[i])!=0: tich*=int(n[i])
    if tich==1:tich=0
    print(tong, tich, sep=' ')