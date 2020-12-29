p = [int(input()) for _ in range(5)]
k = int(input())

for i in range(4):
    for j in range(i+1, 5):
        if p[j] - p[i] > k:
            print(':(')
            exit()
print('Yay!')