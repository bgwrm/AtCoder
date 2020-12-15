s = input()
q = int(input())
query = [input() for i in range(q)]
rev = False
b = ''
a = ''

for qu in query:
    if qu[0] == '1':
        rev = not rev
    elif (qu[2] == '1' and not rev) or (qu[2] == '2' and rev):
        b += qu[4]
    else:
        a += qu[4]

s = b[::-1] + s + a

print(s[::-1] if rev else s)