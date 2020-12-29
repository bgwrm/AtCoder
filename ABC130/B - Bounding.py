n, x = (int(_) for _ in input().split())
l = [int(_) for _ in input().split()]
now, ans = 0, 1

for i in l:
    now += i
    if now <= x:
        ans += 1
print(ans)