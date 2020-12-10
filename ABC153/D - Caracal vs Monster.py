h = int(input())
count = 1

while h > 1:
    h //= 2
    count += 1
    if h == 0:
        count -= 1

print(2 ** (count) - 1)