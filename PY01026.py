for t in range(int(input())):
    s1, s2= input(), input()
    if sorted(s1) == sorted(s2):
        print(f"Test {t+1}: YES")
    else: print(f"Test {t+1}: NO")