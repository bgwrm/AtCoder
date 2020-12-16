n, k = (int(_) for _ in input().split())
print(min(n%k, abs(n%k-k)))