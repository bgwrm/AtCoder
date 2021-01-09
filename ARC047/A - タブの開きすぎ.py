n, l = (int(_) for _ in input().split())
s = input()
now, ans = 1, 0
for i in s:
    if i == '+':
        now += 1
        if now > l:
            ans += 1
            now = 1
    else:
        now -= 1
print(ans)