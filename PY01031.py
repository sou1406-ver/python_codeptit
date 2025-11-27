HE_SO = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for t in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if a == 0:
        print(0)
        continue
    c = []
    while a > 0:
        du = a % b
        ky_tu = HE_SO[du]
        c.append(ky_tu)
        a //= b
    print("".join(c[::-1]))