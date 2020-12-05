n = input()
num = 0

for i in range(len(n)):
    num += int(n[i])

print('No' if num % 9 else 'Yes')