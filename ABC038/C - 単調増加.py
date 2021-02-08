# しゃくとり
n = int(input())
a = [int(_) for _ in input().split()]
ans, i = 1, 0
for j in range(1, n):
    if a[j-1] >= a[j]:
        i = j
    ans += j-i+1
print(ans)