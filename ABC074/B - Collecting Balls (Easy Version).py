n = int(input())
k = int(input())
x = [int(_) for _ in input().split()]
ans = 0

for i in range(n):
    ans += min(2*abs(x[i]),2*abs(k-x[i]))
print(ans)