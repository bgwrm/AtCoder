s = int(input())
mod = 10 ** 9 + 7
ans = [0] * (s+1)

if s < 3:
    print(0)
    exit()

ans[3] = 1

for i in range(4, s+1):
    ans[i] = (ans[i-3] + ans[i-1]) % mod

print(ans[s])