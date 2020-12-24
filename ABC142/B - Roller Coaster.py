n, k = (int(_) for _ in input().split())
h = [int(_) for _ in input().split()]
ans = 0
for i in h:
    if i >= k:
        ans += 1

print(ans)