a, b, k = (int(_) for _ in input().split())
ans = []
for i in range(a, a+k):
    if i <= b:
        ans += [i]
for i in range(b-k+1, b+1):
    if i >= a:
        ans += [i]

for i in sorted(set(ans)):
    print(i)