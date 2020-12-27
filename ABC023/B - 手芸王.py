n = int(input())
s = input()
now = 'b'

for i in range(1, n+2):
    if now == s:
        print(i-1)
        exit()
    if i%3 == 1:
        now = 'a' + now + 'c'
    elif i%3 == 2:
        now = 'c' + now + 'a'
    else:
        now = 'b' + now + 'b'
print(-1)