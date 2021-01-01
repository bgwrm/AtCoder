n = int(input())
ab = sorted([[int(_) for _ in input().split()] for i in range(n)], key=lambda x: x[1])
t = 0

for i in ab:
    t += i[0]
    if t > i[1]:
        print('No')
        exit()
print('Yes')