n = int(input())
h = [int(_) for _ in input().split()]
ans = 0
now = 0

for i in range(n-1):
    if h[i] >= h[i+1]:
        now += 1
        ans = max(now, ans)
    else:
        now = 0

print(ans)