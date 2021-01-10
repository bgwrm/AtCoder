s = input()
l = [['I','i'],['C','c'],['T','t']]
c = 0
for i in s:
    if i in l[c]:
        c += 1
    if c == 3:
        print('YES')
        exit()
print('NO')