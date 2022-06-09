k = int(input())
dp, mod = [0]*(k+1), 10**9+7
if k%9: exit(print(0))
dp[0] = 1
for i in range(1,k+1):
    for j in range(1, min(i, 9)+1):
        dp[i] = (dp[i]+dp[i-j])%mod
print((dp[k])%mod)