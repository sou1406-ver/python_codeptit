def is_hamming(n):
    if n < 1: return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1

def hamming_index(n):
    if not is_hamming(n):
        print('Not in sequence')
        return
    h = [1]
    i2 = i3 = i5 = 0

    while h[-1] < n:
        next2 = h[i2] * 2
        next3 = h[i3] * 3
        next5 = h[i5] * 5

        x = min(next2, next3, next5)

        h.append(x)

        if x == next2: i2 += 1
        if x == next3: i3 += 1
        if x == next5: i5 += 1

    print(h.index(n) + 1)


for _ in range(int(input())):
    n=int(input())
    hamming_index(n)