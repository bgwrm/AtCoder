n = int(input())
a = [int(_) for _ in input().split()]
h = 2**(n-1)
a1, a2 = a[:h], a[h:]
print(a.index(min(max(a1),max(a2)))+1)