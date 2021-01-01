import math
n = int(input())
t = [int(input()) for _ in range(n)]
ans = 1
for i in range(n):
    ans = (ans*t[i])//math.gcd(ans,t[i])
print(ans)