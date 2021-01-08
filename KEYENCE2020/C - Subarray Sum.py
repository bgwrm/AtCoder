n, k, s = (int(_) for _ in input().split())
print(*([s]*k + ([1]*(n-k) if s==10**9 else [s+1]*(n-k))))