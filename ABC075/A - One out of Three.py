abc = input().split()
for i in range(3):
    if abc.count(abc[i]) == 1:
        print(abc[i])
        exit()