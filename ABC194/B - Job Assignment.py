n = int(input())
ab = [[int(_) for _ in input().split()] for i in range(n)]
a, b = [list(i) for i in zip(*ab)]
min_a, min_b = min(a), min(b)
l_a, l_b = [i for i, x in enumerate(a) if x == min_a], [i for i, x in enumerate(b) if x == min_b]
s_a, s_b = sorted(list(set(a))), sorted(list(set(b)))
if len(l_a) == len(l_b) == 1 and l_a[0] == l_b[0]:
    print(min(min_a+min_b, max(min_a, s_b[1]), max(s_a[1], min_b)))
else:
    print(max(min_a,min_b))