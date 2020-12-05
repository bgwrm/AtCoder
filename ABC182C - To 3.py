n = input()
one = n.count('1') + n.count('4') + n.count('7')
two = n.count('2') + n.count('5') + n.count('8')
sum = 0

for i in range(len(n)):
    sum += int(n[i])

if sum % 3 == 0:
    print(0)
elif sum % 3 == 1:
    if one >= 1 and len(n) > 1:
        print(1)
    elif two >= 2 and len(n) > 2:
        print(2)
    else:
        print(-1)
else:
    if two >= 1 and len(n) > 1:
        print(1)
    elif one >= 2 and len(n) > 2:
        print(2)
    else:
        print(-1)