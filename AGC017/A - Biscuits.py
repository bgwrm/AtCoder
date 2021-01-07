n, p = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
odd = 0

for i in a:
    if i%2 == 1:
        odd = 1
        break

if p == odd == 0:
    print(2**n)
elif odd == 0:
    print(0)
else:
    print(2**(n-1))