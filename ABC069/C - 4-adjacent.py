n = int(input())
a = [int(_) for _ in input().split()]
x, y, z = 0, 0, 0

for i in a:
    if i%4 == 0:
        x += 1
    elif i%2 == 0:
        y = 1
    else:
        z += 1

print('Yes' if x >= y + z - (x+y+z)%2 else 'No')