from collections import Counter
n = int(input())
s = [int(_) for _ in input().split()]
s1 = s[::2]
s2 = s[1::2]
c1 = Counter(s1).most_common()
c2 = Counter(s2).most_common()

if c1[0][0] == c2[0][0]:
    if len(c1) == 1 and len(c2) == 1:
        print(n//2)
    else:
        print(min(n-c1[1][1]-c2[0][1], n-c1[0][1]-c2[1][1]))
else:
    print(n-c1[0][1]-c2[0][1])