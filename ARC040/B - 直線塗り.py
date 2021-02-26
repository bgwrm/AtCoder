n, r = (int(_) for _ in input().split())
s = input()
i, ans = 0, max(0, s.rfind('.')-r+1)
while i < n:
    if s[i] == '.':
        i += r-1
        ans += 1
    i += 1
print(ans)