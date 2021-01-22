n = int(input())
a = [int(_) for _ in input().split()]
b = 0
for i in a:
    b ^= i
print(*(i^b for i in a))