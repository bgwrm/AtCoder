import bisect

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, num + 1, 2):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True

q = int(input())
li = []
for i in range(3, 10**5+1, 2):
    if is_prime(i) and is_prime((i+1)//2):
        li += [i]
for i in range(q):
    l, r = (int(_) for _ in input().split())
    print(bisect.bisect_right(li, r)-bisect.bisect_left(li, l))