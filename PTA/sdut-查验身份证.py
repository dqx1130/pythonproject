# 校验权重
weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
# Z值对应的校验码
z_to_m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

# 检查身份证是否合法
def is_valid_id(id_number):
    # 检查前17位是否为数字
    if not id_number[:17].isdigit():
        return False
    # 计算校验码
    weighted_sum = sum(int(id_number[i]) * weights[i] for i in range(17))
    z_value = weighted_sum % 11
    # 比较校验码
    return id_number[17] == z_to_m[z_value]

# 输入
n = int(input())  # 输入身份证数量
invalid_ids = []  # 存储无效身份证号码

for _ in range(n):
    id_number = input().strip()
    if not is_valid_id(id_number):
        invalid_ids.append(id_number)

# 输出
if invalid_ids:
    print("\n".join(invalid_ids))  # 输出有问题的身份证号码
else:
    print("All passed")  # 所有身份证号码均合法
