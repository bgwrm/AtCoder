n = int(input())
for i in range(1,10**2+1):
    if i**3 == n:
        print('YES')
        exit()
print('NO')