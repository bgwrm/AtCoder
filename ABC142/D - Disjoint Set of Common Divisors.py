import math
a, b = (int(_) for _ in input().split())
gcd = math.gcd(a,b)
l = [1]
i = 2
while i*i <= gcd:
    while gcd%i == 0:
        l += [i]
        gcd //= i
    i += 1
l += [gcd]
print(len(set(l)))