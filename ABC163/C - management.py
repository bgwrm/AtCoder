n = int(input())
a = [int(_) for _ in input().split()]
ans = [0] * n

for i in a:
    ans[i-1] += 1

for i in range(n):
    print(ans[i])