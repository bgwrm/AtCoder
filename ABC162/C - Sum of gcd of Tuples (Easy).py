import math
k = int(input())
ans = 0

for i in range(1, k+1):
    for j in range(1, k+1):
        n = math.gcd(i, j)
        for k in range(1, k+1):
            ans += math.gcd(n, k)

print(ans)