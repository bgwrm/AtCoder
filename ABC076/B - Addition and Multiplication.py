n = int(input())
k = int(input())
ans = 1

for i in range(n):
    if 2 * ans < ans + k:
        ans *= 2
    else:
        ans += k
print(ans)