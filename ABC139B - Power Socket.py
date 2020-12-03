AB = [int(x) for x in input().split()]

for i in range(21):
    if i * AB[0] - i + 1 >= AB[1] :
        print(i)
        exit()