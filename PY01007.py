import math

for t in range(int(input())):
    n, x, m = [float(x) for x in input().split()]
    print(math.ceil(math.log(m/n, (100+x)/100)))
