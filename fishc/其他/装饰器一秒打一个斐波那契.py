import time
def delay(func):
    def call_func():
        time.sleep(1)
        func()
    return call_func
def fib():
    back1, back2 = 0, 1
    @ delay
    def func():
        nonlocal back1, back2
        back1, back2 = back2, back1 + back2
        print(back1, end=' ')
    return func
def get_fib(n):
    f = fib()
    for i in range(n):
        f()
n = int(input("请输入需要获取的斐波那契数："))
get_fib(n)