n, x, y = (int(_) for _ in input().split())
ans = [0] * (n-1)

for i in range(0, n-1):
    for j in range(i+1, n):
        ans[min(abs(j-i), abs(x-1-i) + 1 + abs(y-1-j))-1] += 1

for i in range(n-1):
    print(ans[i])