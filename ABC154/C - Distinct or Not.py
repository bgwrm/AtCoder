n = int(input())
a = [int(_) for _ in input().split()]
print('YES' if len(set(a)) == n else 'NO')