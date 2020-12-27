import math
n, m = (int(_) for _ in input().split())
mod = 10 ** 9 + 7
ans = 1

if abs(n - m) > 1:
    print(0)
else:
    for i in range(2, min(n+1, m+1)):
        ans = ans * i % mod
    if n == m:
        print(2 * ans * ans % mod)
    else:
        print(ans * ans * max(n, m) % mod)