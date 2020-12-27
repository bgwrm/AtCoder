import itertools
n = int(input())
s = [input() for _ in range(n)]
l = [0] * 5
ans = 0

for i in s:
    if i[0] == 'M':
        l[0] += 1
    elif i[0] == 'A':
        l[1] += 1
    elif i[0] == 'R':
        l[2] += 1
    elif i[0] == 'C':
        l[3] += 1
    elif i[0] == 'H':
        l[4] += 1

for i in itertools.combinations(l, 3):
    ans += i[0] * i[1] * i[2]

print(ans)