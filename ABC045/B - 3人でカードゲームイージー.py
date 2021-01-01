a = input()
b = input()
c = input()
now = 'a'

while True:
    if now == 'a':
        if len(a) == 0:
            print('A')
            exit()
        now = a[0]
        a = a[1:]
    elif now == 'b':
        if len(b) == 0:
            print('B')
            exit()
        now = b[0]
        b = b[1:]
    else:
        if len(c) == 0:
            print('C')
            exit()
        now = c[0]
        c = c[1:]