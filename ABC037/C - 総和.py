n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
p = sum(a[:k])
ans = p
for i in range(k,n):
    p += a[i] - a[i-k]
    ans += p
print(ans)