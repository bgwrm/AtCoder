from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
c = Counter(s).most_common()
print(c[0][0])