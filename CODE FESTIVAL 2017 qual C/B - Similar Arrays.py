n = int(input())
a = [int(_) for _ in input().split()]
c = sum(i%2 == 0 for i in a)
print(3**n-2**c)