n = int(input())
a = [int(input()) for _ in range(n)]
sorted_a = sorted(a, reverse=True)
a1, a2 = sorted_a[0], sorted_a[1]

for i in a:
    print(a1 if i != a1 else a2)