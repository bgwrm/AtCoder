n, m = (int(_) for _ in input().split())
n_max, n_min = 10**5, 0

for i in range(m):
    l, r = (int(_) for _ in input().split())
    n_max = min(n_max, r)
    n_min = max(n_min, l)

print(max(n_max-n_min+1, 0))