e = [int(_) for _ in input().split()]
b = int(input())
l = [int(_) for _ in input().split()]
m, bo = 0, 0
for i in l:
    if i in e:
        m += 1
    elif i == b:
        bo = 1
print(1 if m == 6 else 2 if m == 5 and bo == 1 else 3 if m == 5 else 4 if m == 4 else 5 if m == 3 else 0)