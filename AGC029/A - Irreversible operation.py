s = input()
n = 0
ans = 0

for i in range(len(s)):
    if s[i] == 'W':
        ans += i - n
        n += 1

print(ans)