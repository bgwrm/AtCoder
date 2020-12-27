from collections import Counter
n = int(input())
a = Counter([int(_) for _ in input().split()])
l = sorted([i[0] for i in a.items() if i[1] >= 2], reverse=True)

if len(l) < 2:
    print(0)
else:
    if a[l[0]] >= 4:
        print(l[0]**2)
    else:
        print(l[0]*l[1])