s = input() + '0'
a = s[0]
c = 1
ans = ''

for i in range(1, len(s)):
    if s[i] == a:
        c += 1
    else:
        ans += a + str(c)
        a = s[i]
        c = 1
ans += str(c)

print(ans[:-1])