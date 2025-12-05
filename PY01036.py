for t in range(int(input())):
    n = int(input())
    sum=0
    for i in range(n,0,-2): sum+= 1/i
    print(f"{sum:.6f}")