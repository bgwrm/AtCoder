l, r = (int(_) for _ in input().split())
ans = []

if r - l >= 2019:
    print(0)
    exit()

for i in range(l,r+1):
    for j in range(l, r+1):
        if i == j:
            continue
        else:
            ans += [(i*j)%2019]
print(min(ans))