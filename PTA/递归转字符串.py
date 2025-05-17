def intToString(num):
    if num // 10 == 0:
        return f'{num}'
    return intToString(num // 10) + f'{num % 10}'


n = int(input())
for i in range(n):
    num = int(input())
    if num >= 0:
        print(intToString(num))
    else:
        num = abs(num)
        print('-'+intToString(num))

