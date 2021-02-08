n, k, m, r = (int(_) for _ in input().split())
s = sorted([int(input()) for _ in range(n-1)], reverse=True)
p = k*r-sum(s[:k-1])
print(-1 if p > m else 0 if sum(s[:k]) >= k*r else max(p, 0))