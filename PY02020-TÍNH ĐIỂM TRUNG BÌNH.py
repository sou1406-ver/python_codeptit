n=int(input())
a=[float(a) for a in input().split()]
b=[float(b) for b in a if b!= min(a) and b!=max(a) ]
print(f"{(sum(b)/len(b)):.2f}")
