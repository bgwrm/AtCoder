s = input().split('+')
c = 0
for i in s:
    if i.count('0') > 0:
        c += 1
print(len(s)-c)