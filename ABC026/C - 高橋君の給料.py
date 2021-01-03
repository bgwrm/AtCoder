n = int(input())
b = [int(input()) for _ in range(n-1)]
s = [1] * n

for i in range(n, 0, -1):
    l = [s[x+1] for x, y in enumerate(b) if y == i]
    if len(l) == 0:
        s[i-1] = 1
    else:
        s[i-1] = max(l) + min(l) + 1
print(s[0])