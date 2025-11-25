n =input()
if len(n)>3:
    for i in range(len(n)-3, 0,-3):
        n=n[:i] + ',' +n[i:]
    print(n)
else: print(n)