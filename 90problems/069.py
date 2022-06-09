n, k = (int(_) for _ in input().split())
mod = 10**9+7
if n == 1: print(k)
elif n == 2: print(k*(k-1))
else: print((k*(k-1)*pow(k-2, n-2, mod))%mod)