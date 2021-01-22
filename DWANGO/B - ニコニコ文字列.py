s = input().replace('25', 'n')
ans = c = 0
for i in s:
    if i == 'n':
        c += 1
        ans += c
    else:
        c = 0
print(ans)