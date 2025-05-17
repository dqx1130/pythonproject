import sys
def fib():
    def func():
        global back_1,back_2
        tmp = back_2
        back_1,back_2 = back_2,back_1+back_2
        return tmp
    return func
back_1 ,back_2 = 0,1

for line in sys.stdin:
    f = fib()
    print(f())