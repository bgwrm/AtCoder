import itertools
n = list(input())
op = itertools.product(['+', '-'], repeat=3)
for i in op:
    s = n[0]+i[0]+n[1]+i[1]+n[2]+i[2]+n[3]
    if eval(s) == 7:
        print(s+'=7')
        exit()