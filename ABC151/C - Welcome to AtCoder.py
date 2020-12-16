n, m = (int(_) for _ in input().split())
ps = [input().split() for i in range(m)]
a = [0] * (n+1)
p = [0] * (n+1)
c = 0

for i in ps:
    if i[1] == 'WA' and a[int(i[0])] == 0:
        p[int(i[0])] += 1
    elif i[1] == 'AC':
        a[int(i[0])] = 1

for i in range(len(a)):
    if a[i] == 1:
        c += p[i]

print(sum(a), c)