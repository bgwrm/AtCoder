n, h, w = (int(_) for _ in input().split())
ans = 0
for i in range(n):
    a, b = (int(_) for _ in input().split())
    if a >= h and b >= w:
        ans += 1
print(ans)