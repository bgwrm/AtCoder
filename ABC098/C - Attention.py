n = int(input())
s = input()
now = s.count('E')
ans = [now]

for i in s:
    if i == 'E':
        now -= 1
    else:
        now += 1
    ans += [now]

print(min(ans))