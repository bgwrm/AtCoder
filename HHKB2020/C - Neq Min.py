n = int(input())
p = [int(_) for _ in input().split()]
now = 0
s = set()
for i in p:
    s.add(i)
    while now in s:
        now += 1
    print(now)