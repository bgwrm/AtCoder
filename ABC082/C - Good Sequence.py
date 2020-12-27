from collections import Counter
n = int(input())
a = Counter([int(_) for _ in input().split()])
ans = 0

for i in a.items():
    if i[0] < i[1]:
        ans += i[1] - i[0]
    elif i[0] > i[1]:
        ans += i[1]

print(ans)