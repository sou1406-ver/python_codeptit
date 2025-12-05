
def ans(n):
    if int(n)%7==0 :
        return int(n)
    for _ in range(1000):
        n=str(int(n)+ int(n[::-1]))
        if int(n) %7==0:
            return int(n)
    return -1
for _ in range(int(input())):
    n=input()
    print(ans(n))

