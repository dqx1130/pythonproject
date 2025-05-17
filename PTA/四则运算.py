# 定义四则运算的函数
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "divided by zero"
    return x / y

# 用字典模拟 switch 功能
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# 读取输入
num1 = float(input())  # 第一个数字
operator = input()     # 四则运算符
num2 = float(input())  # 第二个数字

# 判断并计算结果
if operator in operations:
    result = operations[operator](num1, num2)
    if operator == '/' and num2 == 0:
        print(result)  # 输出 "divided by zero"
    elif isinstance(result, float):
        print(f"{result:.2f}")  # 小数保留2位
    else:
        print(result)
else:
    print("Invalid operator")  # 如果运算符无效，输出提示
