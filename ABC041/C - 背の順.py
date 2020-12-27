n = int(input())
a = [(int(_), i) for i, _ in enumerate(input().split(), 1)]

for h in sorted(a, reverse=True):
    print(h[1])