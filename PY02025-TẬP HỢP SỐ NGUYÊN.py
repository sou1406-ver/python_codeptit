n, m= map(int, input().split())
a=sorted(set([int(x) for x in input().split()]))
b=sorted(set([int(x) for x in input().split()]))
for i in a:
    if i in b: print(i, end=' ')
print()
for i in a:
    if not i in b: print(i, end=' ')
print()
for  i in b:
    if not i in a: print(i, end=' ')
