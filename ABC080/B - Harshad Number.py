n = input()
p = 0
for i in n:
    p += int(i)
print('Yes' if int(n)%p == 0 else 'No')