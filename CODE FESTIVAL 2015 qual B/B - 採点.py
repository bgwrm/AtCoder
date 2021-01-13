from collections import Counter
n, m = (int(_) for _ in input().split())
a = Counter([int(_) for _ in input().split()]).most_common()
print(a[0][0] if a[0][1] > n/2 else '?')