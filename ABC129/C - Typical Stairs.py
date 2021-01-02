n, m = (int(_) for _ in input().split())
a = set([int(input()) for _ in range(m)])
mod = 10 ** 9 + 7
ans = [1] + [0] * (n+1)

for i in range(n):
    if i+1 not in a:
        ans[i+1] += ans[i]
        ans[i+1] %= mod
    if i+2 not in a:
        ans[i+2] += ans[i]
        ans[i+2] %= mod

print(ans[n]%mod)