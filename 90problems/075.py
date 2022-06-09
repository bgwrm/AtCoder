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

k, l = 1, len(prime_factorize(int(input())))
for i in range(10**6):
    if k >= l:
        print(i)
        exit()
    k *= 2