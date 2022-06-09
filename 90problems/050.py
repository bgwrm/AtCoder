from operator import mul
from functools import reduce
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n, l = (int(_) for _ in input().split())
ans, mod = 1, 10**9+7
for i in range(1, n//l+1):
    j = n-i*l
    ans = (ans+cmb(i+j, i))%mod
print(ans%mod)