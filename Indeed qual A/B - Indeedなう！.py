n = int(input())
s = [sorted(list(input())) for _ in range(n)]
a = sorted(list('indeednow'))
for i in s:
    print('YES' if i == a else 'NO')