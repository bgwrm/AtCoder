n, m = (int(_) for _ in input().split())
if 2 * n >= m:
    print(m // 2)
else:
    print(n + (m - 2 * n) // 4)