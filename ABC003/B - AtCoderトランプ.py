s = input()
t = input()
l = ['a','t','c','o','d','e','r']

for i in range(len(s)):
    if s[i] != t[i]:
        if s[i] != '@' and t[i] != '@':
            print('You will lose')
            exit()
        elif s[i] != '@':
            if s[i] not in l:
                print('You will lose')
                exit()
        elif t[i] != '@':
            if t[i] not in l:
                print('You will lose')
                exit()
print('You can win')