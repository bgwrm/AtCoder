from collections import Counter
n = int(input())
s = [input() for i in range(n)]
c = Counter(s)
t = c.most_common()[0][1]
l = sorted(set(s))

for a in l:
    if c[a] == t:
        print(a)