n = int(input())
l = ['1', '2', '3', '4', '5', '6']
for i in range(n%30):
    c1 = l[i%5]
    c2 = l[i%5+1]
    l[i%5+1] = c1
    l[i%5] = c2
print(''.join(l))