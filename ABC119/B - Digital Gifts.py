n = int(input())
xu = [input().split() for i in range(n)]
ans = 0

for i in range(n):
    if xu[i][1] == 'JPY':
        ans += int(xu[i][0])
    else:
        ans += 380000.0 * float(xu[i][0])

print(ans)