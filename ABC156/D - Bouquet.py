n, a, b = (int(_) for _ in input().split())
mod = 10**9+7
ans, p, q = pow(2, n, mod)-1, 1, 1
for i in range(1, b+1):
    p = p*(n-i+1)%mod
    q = q*i%mod
    if i == a or i==b:
        ans -= p*pow(q, mod-2, mod)
print(ans%mod)