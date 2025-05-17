def calculate(expr):
    stack = []
    
    for char in expr:
        if char.isdigit():
            # 如果是数字，直接入栈
            stack.append(float(char))
        elif char in '+-*/':
            # 如果是运算符，从栈中弹出两个操作数
            b = stack.pop()
            a = stack.pop()
            
            # 根据运算符进行计算
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    
    # 返回最终结果
    return stack[0]

# 处理多组输入直到EOF
while True:
    try:
        expr = input().strip()
        result = calculate(expr)
        print(f"{result:.2f}")
    except EOFError:
        break