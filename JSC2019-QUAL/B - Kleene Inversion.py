from collections import Counter
n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
c = sorted(list(Counter(a).items()), reverse=True)
mod = 10**9 + 7
ans = s = 0
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            if i < j:
                ans += k*(k+1)//2
            else:
                ans += (k-1)*k//2
            ans %= mod
print(ans)