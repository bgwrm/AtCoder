s = input()
s1, s2 = s[0], ''
ans = 1

for i in range(1, len(s)):
    s2 += s[i]
    if s1 != s2:
        s1 = s2
        s2 = ''
        ans += 1

print(ans)