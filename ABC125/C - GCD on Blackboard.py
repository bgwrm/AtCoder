from math import gcd
n = int(input())
a = [int(_) for _ in input().split()]
ans, l, r = 0, [0], [0]
for i in range(n-1):
    l += [gcd(a[i], l[i])]
    r += [gcd(a[-i-1], r[i])]
for i in range(n):
    ans = max(gcd(l[i], r[-i-1]), ans)
print(ans)