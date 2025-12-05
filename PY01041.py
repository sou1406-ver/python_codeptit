def check(n):
    i=0
    if len(n)<3: return 'NO'
    while i<len(n)-1 and n[i]<n[i+1]:i+=1
    while i<len(n)-1 and n[i]>n[i+1]:i+=1
    if i== len(n)-1: return 'YES'
    else: return 'NO'

for _ in range(int(input())):
    n=input()
    print(check(n))