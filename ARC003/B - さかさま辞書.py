n = int(input())
s = sorted([input()[::-1] for _ in range(n)])

for i in s:
    print(i[::-1])