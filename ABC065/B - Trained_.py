n = int(input())
a = [int(input()) for _ in range(n)]
now = 1
time = 1

while time < 10**6:
    if now == a[now-1]:
        print(-1)
        exit()
    now = a[now-1]
    if now == 2:
        print(time)
        exit()
    time += 1

print(-1)