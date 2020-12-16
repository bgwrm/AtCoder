n = int(input())
a1 = [int(_) for _ in input().split()]
a2 = [int(_) for _ in input().split()]
ans = 0
for i in range(n):
    n = sum(a1[:i+1]) + sum(a2[i:])
    if n > ans:
        ans = n
print(ans)