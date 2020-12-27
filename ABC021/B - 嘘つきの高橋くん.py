from collections import Counter
n = int(input())
a, b = (int(_) for _ in input().split())
k = int(input())
p = [int(_) for _ in input().split()] + [a] + [b]
c = Counter(p).most_common()[0][1]
print('YES' if c == 1 else 'NO')