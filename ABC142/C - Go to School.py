n = int(input())
a = [int(_) for _ in input().split()]
ans = [''] * n

for i in range(n):
    ans[a[i]-1] = str(i + 1)

print(' '.join(ans))