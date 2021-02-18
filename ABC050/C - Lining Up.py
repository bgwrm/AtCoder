import heapq
n = int(input())
a = [int(_) for _ in input().split()]
heapq.heapify(a)
c = n%2
if c and heapq.heappop(a) != 0:
    print(0)
    exit()
for i in range(1, n, 2):
    if heapq.heappop(a) != i+c or heapq.heappop(a) != i+c:
        print(0)
        exit()
print(pow(2, n//2, 10**9+7))