def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

# n = eval(input())
res = 0
n = 5
print(factorial(abs(int(n))))
