n = int(input())
s = input()
x = ''
for i in s:
    x += i
    if x[-3:] == 'fox':
        x = x[:-3]
print(len(x))