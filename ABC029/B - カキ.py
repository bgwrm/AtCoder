s = [input() for _ in range(12)]
ans = 0
for i in s:
    if i.count('r'):
        ans += 1
print(ans)