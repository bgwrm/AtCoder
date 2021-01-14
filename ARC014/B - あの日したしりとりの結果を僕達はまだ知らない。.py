n = int(input())
c, s = '', set()
for i in range(n):
    w = input()
    if w in s or (i > 0 and c != w[0]):
        print('WIN' if i%2 else 'LOSE')
        exit()
    c = w[-1]
    s.add(w)
else:
    print('DRAW')