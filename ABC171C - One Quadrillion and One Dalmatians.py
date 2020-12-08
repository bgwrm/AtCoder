n = int(input())
alphabet = [chr(ord('a') + i) for i in range(26)]
ans = ''

while True:
    n -= 1
    ans += alphabet[n % 26]
    n //= 26
    if n == 0:
        break

print(ans[::-1])