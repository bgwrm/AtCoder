import itertools
n, m, l = (int(_) for _ in input().split())
pqr = [int(_) for _ in input().split()]
print(max((n//i)*(m//j)*(l//k) for i, j, k in itertools.permutations(pqr, 3)))