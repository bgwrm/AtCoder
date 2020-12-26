n = int(input())
i = 0

if n < 4:
    print('No')
    exit()

while 4 * i <= n:
    if (n-4*i)%7 == 0:
        print('Yes')
        exit()
    i += 1
print('No')