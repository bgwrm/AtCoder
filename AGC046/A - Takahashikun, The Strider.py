x = int(input())
for i in range(1,180):
    if (i*360/x).is_integer():
        print(int(i*360/x))
        exit()