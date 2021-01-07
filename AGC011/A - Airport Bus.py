n, c, k = (int(_) for _ in input().split())
t = sorted([int(input()) for _ in range(n)])
p, l, ans = 0, t[0], 1

for i in t:
    if i <= l+k:
        p += 1
    if p > c or i > l+k:
        ans += 1
        p = 1
        l = i

print(ans)