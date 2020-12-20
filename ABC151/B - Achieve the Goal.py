n, k, m = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
p = m*n - sum(a)
print(0 if p <= 0 else p if p <= k else -1)