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

n = int(input())
s = str(n)
wa = sum(int(s[i]) for i in range(len(s)))
if n == 1:
    print('Not Prime')
elif is_prime(n):
    print('Prime')
elif int(s[-1])%2 == 0 or int(s[-1]) == 5 or wa%3 == 0:
    print('Not Prime')
else:
    print('Prime')