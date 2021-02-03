n = int(input())
s = t = input()
for i in range(50):
    t = t.replace('()', '')
print('('*t.count(')')+s+')'*t.count('('))