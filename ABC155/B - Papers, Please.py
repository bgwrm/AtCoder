n = int(input())
a = [int(_) for _ in input().split()]

for i in a:
    if i%2 == 0:
        if i%3 != 0 and i%5 != 0:
            print('DENIED')
            exit()

print('APPROVED')