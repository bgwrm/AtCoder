n, k = (int(_) for _ in input().split())
a = [int(input()) for _ in range(n)]
ans = c = p = 0
for i in a:
    if i > p: c += 1
    else: c = 1
    if c >= k: ans += 1
    p = i
print(ans)