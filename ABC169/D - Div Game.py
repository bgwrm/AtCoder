def factorize(n):
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
l = factorize(n)
ans = 0
for i in set(l):
    c = l.count(i)
    d = 2
    while c > 0:
        c -= d
        d += 1
        ans += 1
print(ans)