n = int(input())
ans = 1
for i in range(1, n+1):
    if input() == 'OR':
        ans += 2**i
print(ans)