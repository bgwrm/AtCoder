from collections import Counter

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n = int(input())
mod = 10**9 + 7
ans, l = 1, []
for i in range(2, n+1):
    l += prime_factorize(i)
c = Counter(l).values()
for i in c:
    ans *= i+1
    ans %= mod
print(ans)