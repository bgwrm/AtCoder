s = input()
now, ans = 0, 0
for i in s:
    if i == 'A' or i == 'C' or i == 'G' or i == 'T':
        now += 1
        ans = max(ans, now)
    else:
        now = 0

print(ans)