n, m = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
ans = n - sum(a)
print(ans if ans >= 0 else '-1')