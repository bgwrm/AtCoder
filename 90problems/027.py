a = set()
for i in range(int(input())):
    s = input()
    if s not in a:
        print(i+1)
        a.add(s)