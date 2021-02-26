a = b = 0
for s in input():
    if s == 'S': a += 1
    elif a > 0: a -= 1
    else: b += 1
print(a+b)