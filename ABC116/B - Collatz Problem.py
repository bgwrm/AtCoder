s = int(input())
a = [s]

while True:
    if s%2 == 0:
        s /= 2
    else:
        s = 3*s + 1
    if s in a:
        print(len(a)+1)
        exit()
    a += [s]