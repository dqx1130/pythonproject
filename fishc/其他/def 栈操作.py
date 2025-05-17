list = []
def push():
    value = input("请输入将要压入栈中的值：")
    list.append(value)
    print("栈")
    for each in reversed(list):
        print(each,end = "\n")
def pop():
    print(list.pop())
    print("栈")
    for each in reversed(list):
        print(each,end = "\n")
def top():
    if len(list) == 0:
        print("栈已空~")
    else:
        print(list[-1])
while True:
    order = input("请输入指令（push/pop/top/exit）：")
    if order == "exit":
        exit()
    elif order == "push":
        push()
    elif order == "pop":
        pop()
    elif order == "top":
        top()
