n = int(input())
x = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(9):
        if x[i][j] == 'x':
            ans += 1
        elif i == 0 and x[i][j] == 'o':
            ans += 1
        elif i > 0 and x[i][j] == 'o' and x[i-1][j] != 'o':
            ans += 1
print(ans)