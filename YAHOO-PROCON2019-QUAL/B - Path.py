from collections import Counter
ab = [[int(_) for _ in input().split()] for i in range(3)]
print('NO' if Counter(sum(ab,[])).most_common()[0][1] == 3 else 'YES')