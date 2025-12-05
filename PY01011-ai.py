digits = ['0','2','4','6','8']

def generate_even_palindromes(max_len, limit):
    res = []
    for length in range(2, max_len+1, 2):  # only even length
        half = length // 2
        for num in range(10**(half-1), 10**half):
            s = str(num)
            if any(c not in digits for c in s):
                continue
            p = int(s + s[::-1])
            if p < limit:
                res.append(p)
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    L = len(str(n))
    res = generate_even_palindromes(L, n)
    print(*res)
