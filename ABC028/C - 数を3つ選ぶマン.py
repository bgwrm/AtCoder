l = sorted([int(_) for _ in input().split()])
ans = []
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            ans.append(l[i]+l[j]+l[k])

ans.sort()
print(ans[-3])