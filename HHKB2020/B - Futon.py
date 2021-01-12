h, w = (int(_) for _ in input().split())
s = [list(input()) for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if i != h-1 and s[i][j] == s[i+1][j] == '.':
            ans += 1
        if j != w-1 and s[i][j] == s[i][j+1] == '.':
            ans += 1
print(ans)