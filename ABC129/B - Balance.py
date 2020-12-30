n = int(input())
w = [int(_) for _ in input().split()]
ans = 10**6

for i in range(n-1):
    ans = min(ans, abs(2*sum(w[:i+1])-sum(w)))

print(ans)