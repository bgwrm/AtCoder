n = int(input())
h = [int(_) for _ in input().split()]
now, ans = 0, 0
for i in h:
    if i >= now:
        now = i
        ans += 1
print(ans)