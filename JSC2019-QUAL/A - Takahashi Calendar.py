m, d = (int(_) for _ in input().split())
ans = 0
for i in range(1,m+1):
    for j in range(1,d+1):
        if j//10 >= 2 and j%10 >= 2 and (j//10)*(j%10) == i:
            ans += 1
print(ans)