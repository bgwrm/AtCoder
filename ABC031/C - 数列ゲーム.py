n = int(input())
a = [int(_) for _ in input().split()]
ans = -2500
for i in range(n):
    ao = ta = -2500
    for j in range(n):
        if i == j:
            continue
        l, r = min(i, j), max(i, j)
        t = a[l:r+1]
        if sum(t[1::2]) > ao:
            ao = sum(t[1::2])
            ta = sum(t[0::2])
    ans = max(ta, ans)
print(ans)