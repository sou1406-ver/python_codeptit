s= input()
def step(n):
    if len(n) ==1: return 0
    tong=0
    for i in range(len(n)):
        tong+= int(n[i])
    return 1 + step(str(tong))
if len(s) ==1: print(1)
else: print(step(s))
