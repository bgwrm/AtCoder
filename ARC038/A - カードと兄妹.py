n = int(input())
a = sorted([int(_) for _ in input().split()],reverse=True)
print(sum(a[0::2]))