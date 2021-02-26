s = input()
ans, l, r = 0, 0, len(s)-1
while True:
    if l == r or l > r:
        exit(print(ans))
    if s[l] == s[r]:
        l += 1
        r -= 1
    elif s[l] == 'x':
        ans += 1
        l += 1
    elif s[r] == 'x':
        ans += 1
        r -= 1
    else:
        exit(print(-1))