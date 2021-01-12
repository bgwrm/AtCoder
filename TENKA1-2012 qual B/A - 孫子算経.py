a, b, c = (int(_) for _ in input().split())
ans = []
for i in range(1,128):
    if i%3 == a and i%5 == b and i%7 == c:
        ans += [i]
for i in ans:
    print(i)